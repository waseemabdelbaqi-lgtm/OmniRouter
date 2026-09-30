"""
Tests for the Anthropic Messages pass-through (/v1/messages).

Runs offline: Firestore and the Anthropic upstream are replaced with in-memory
fakes, so no Firebase credentials or API keys are needed.
Run: python -m pytest testLib/test_messages.py -v
"""
import json
import sys
import types

import httpx
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from .test_utils import test_logger


class FakeSnapshot:
    def __init__(self, doc_id, data):
        self.id = doc_id
        self._data = data

    def to_dict(self):
        return None if self._data is None else dict(self._data)


class FakeDocument:
    def __init__(self, collection, doc_id):
        self._collection = collection
        self._id = doc_id

    def get(self):
        return FakeSnapshot(self._id, self._collection.docs.get(self._id))

    def update(self, data):
        self._collection.docs[self._id].update(data)


class FakeCollection:
    def __init__(self):
        self.docs = {}

    def document(self, doc_id):
        return FakeDocument(self, doc_id)

    def get(self):
        return [FakeSnapshot(k, v) for k, v in self.docs.items()]

    def on_snapshot(self, callback):
        return None


class FakeFirestore:
    def __init__(self):
        self.collections = {}

    def collection(self, name):
        return self.collections.setdefault(name, FakeCollection())


def import_config_without_firebase():
    """Import serverRouter.core.config, stubbing firebase_admin only if config isn't loaded yet."""
    if "serverRouter.core.config" in sys.modules:
        return sys.modules["serverRouter.core.config"]
    saved = {name: sys.modules.get(name) for name in ("firebase_admin", "firebase_admin.credentials", "firebase_admin.firestore")}
    fake_admin = types.ModuleType("firebase_admin")
    fake_admin.credentials = types.SimpleNamespace(Certificate=lambda path: None)
    fake_admin.firestore = types.SimpleNamespace(client=FakeFirestore)
    fake_admin.initialize_app = lambda cred: None
    sys.modules.update({
        "firebase_admin": fake_admin,
        "firebase_admin.credentials": fake_admin.credentials,
        "firebase_admin.firestore": fake_admin.firestore,
    })
    try:
        from serverRouter.core import config
        return config
    finally:
        for name, module in saved.items():
            if module is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = module


config = import_config_without_firebase()
from serverRouter.routes import messages_routes  # noqa: E402

OMNI_KEY = "omni-test-key"
USER_ID = "test-user"

STREAM_EVENTS = [
    ("message_start", {"type": "message_start", "message": {
        "id": "msg_1", "type": "message", "role": "assistant", "model": "claude-sonnet-test", "content": [],
        "stop_reason": None, "usage": {"input_tokens": 12, "cache_creation_input_tokens": 3,
                                       "cache_read_input_tokens": 5, "output_tokens": 1}}}),
    ("content_block_start", {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}),
    ("ping", {"type": "ping"}),
    ("content_block_delta", {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "Hel"}}),
    ("content_block_delta", {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "lo"}}),
    ("content_block_stop", {"type": "content_block_stop", "index": 0}),
    ("message_delta", {"type": "message_delta", "delta": {"stop_reason": "end_turn"}, "usage": {"output_tokens": 7}}),
    ("message_stop", {"type": "message_stop"}),
]
STREAM_BODY = "".join(f"event: {name}\ndata: {json.dumps(data)}\n\n" for name, data in STREAM_EVENTS).encode()

MESSAGE_BODY = {
    "id": "msg_2", "type": "message", "role": "assistant", "model": "claude-sonnet-test",
    "content": [{"type": "tool_use", "id": "toolu_1", "name": "Bash", "input": {"command": "ls"}}],
    "stop_reason": "tool_use", "usage": {"input_tokens": 100, "output_tokens": 20},
}


class FakeUpstream:
    """Records requests and answers like the Anthropic API."""

    def __init__(self):
        self.requests = []
        self.response = None

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        if self.response is not None:
            return self.response
        body = json.loads(request.content)
        if request.url.path == "/v1/messages/count_tokens":
            return httpx.Response(200, json={"input_tokens": 42})
        if body.get("stream"):
            # Split mid-event to exercise the usage parser's line buffering
            chunks = [STREAM_BODY[:37], STREAM_BODY[37:500], STREAM_BODY[500:]]
            return httpx.Response(200, headers={"content-type": "text/event-stream", "request-id": "req_stream"},
                                  stream=httpx.ByteStream(b"".join(chunks)))
        return httpx.Response(200, json=MESSAGE_BODY, headers={"request-id": "req_1"})


class TestMessagesPassThrough:
    @pytest.fixture(autouse=True)
    def setup(self, monkeypatch):
        self.logger = test_logger
        self.db = FakeFirestore()
        self.db.collection("api_keys").docs[OMNI_KEY] = {"userid": USER_ID}
        self.db.collection("users").docs[USER_ID] = {"usage": {"total_tokens": 0, "total_messages": 0}}
        monkeypatch.setattr(config, "db", self.db)
        monkeypatch.setattr(config, "VALID_API_KEYS", {OMNI_KEY})
        monkeypatch.setattr(config, "ANTHROPIC_UPSTREAM_URL", "https://upstream.test")
        monkeypatch.setenv("ANTHROPIC_API_KEY", "upstream-test-key")

        self.upstream = FakeUpstream()
        monkeypatch.setattr(messages_routes, "_upstream_client",
                            httpx.AsyncClient(transport=httpx.MockTransport(self.upstream)))

        app = FastAPI()
        app.include_router(messages_routes.router)
        self.client = TestClient(app)

    def usage(self):
        return self.db.collection("users").docs[USER_ID]["usage"]

    def post(self, body, headers=None, path="/v1/messages"):
        return self.client.post(path, json=body, headers=headers if headers is not None else {"x-api-key": OMNI_KEY})

    def test_non_streaming_passes_body_through(self):
        body = {
            "model": "claude-sonnet-test", "max_tokens": 1024,
            "system": [{"type": "text", "text": "You are Claude Code", "cache_control": {"type": "ephemeral"}}],
            "tools": [{"name": "Bash", "description": "run", "input_schema": {"type": "object"}}],
            "messages": [{"role": "user", "content": [{"type": "text", "text": "list files"}]}],
        }
        response = self.client.post("/v1/messages?beta=true", json=body, headers={
            "x-api-key": OMNI_KEY, "anthropic-version": "2023-06-01", "anthropic-beta": "claude-code-20250219"})

        assert response.status_code == 200
        assert response.json() == MESSAGE_BODY
        assert response.headers["request-id"] == "req_1"

        sent = self.upstream.requests[0]
        assert str(sent.url) == "https://upstream.test/v1/messages"
        assert json.loads(sent.content) == body
        assert sent.headers["x-api-key"] == "upstream-test-key"
        assert sent.headers["anthropic-beta"] == "claude-code-20250219"
        assert "authorization" not in sent.headers
        assert self.usage()["total_tokens"] == 120
        assert self.usage()["total_messages"] == 1

    def test_streaming_is_relayed_unchanged_and_billed(self):
        with self.client.stream("POST", "/v1/messages", json={
                "model": "claude-sonnet-test", "max_tokens": 64, "stream": True,
                "messages": [{"role": "user", "content": "hi"}]}, headers={"x-api-key": OMNI_KEY}) as response:
            assert response.status_code == 200
            assert response.headers["content-type"].startswith("text/event-stream")
            received = b"".join(response.iter_bytes())

        assert received == STREAM_BODY
        # input 12 + cache write 3 + cache read 5 + final cumulative output 7
        assert self.usage()["total_tokens"] == 27

    def test_bearer_auth_accepted(self):
        response = self.post({"model": "claude-sonnet-test", "max_tokens": 8, "messages": []},
                             headers={"Authorization": f"Bearer {OMNI_KEY}"})
        assert response.status_code == 200

    @pytest.mark.parametrize("headers", [{}, {"x-api-key": "wrong"}, {"Authorization": "Bearer wrong"}])
    def test_rejects_bad_or_missing_key(self, headers):
        response = self.post({"model": "claude-sonnet-test", "max_tokens": 8, "messages": []}, headers=headers)
        assert response.status_code == 401
        assert response.json()["type"] == "error"
        assert response.json()["error"]["type"] == "authentication_error"
        assert self.upstream.requests == []

    def test_token_limit_enforced(self, monkeypatch):
        monkeypatch.setattr(config, "MAX_TOKENS", 10)
        self.usage()["total_tokens"] = 10
        response = self.post({"model": "claude-sonnet-test", "max_tokens": 8, "messages": []})
        assert response.status_code == 429
        assert response.json()["error"]["type"] == "rate_limit_error"
        assert self.upstream.requests == []

    def test_omnirouter_alias_is_resolved(self):
        self.post({"model": "claude-3-5-haiku", "max_tokens": 8, "messages": []})
        assert json.loads(self.upstream.requests[0].content)["model"] == "claude-3-5-haiku-20241022"

    def test_non_anthropic_model_rejected(self):
        response = self.post({"model": "gpt-4o", "max_tokens": 8, "messages": []})
        assert response.status_code == 400
        assert response.json()["error"]["type"] == "invalid_request_error"
        assert self.upstream.requests == []

    def test_upstream_errors_pass_through_unbilled(self):
        error = {"type": "error", "error": {"type": "overloaded_error", "message": "Overloaded"}}
        self.upstream.response = httpx.Response(529, json=error, headers={"retry-after": "3"})
        response = self.post({"model": "claude-sonnet-test", "max_tokens": 8, "stream": True, "messages": []})
        assert response.status_code == 529
        assert response.json() == error
        assert response.headers["retry-after"] == "3"
        assert self.usage()["total_tokens"] == 0

    def test_missing_server_key(self, monkeypatch):
        monkeypatch.delenv("ANTHROPIC_API_KEY")
        response = self.post({"model": "claude-sonnet-test", "max_tokens": 8, "messages": []})
        assert response.status_code == 500
        assert response.json()["error"]["type"] == "api_error"

    def test_invalid_json(self):
        response = self.client.post("/v1/messages", content=b"not json",
                                    headers={"x-api-key": OMNI_KEY, "content-type": "application/json"})
        assert response.status_code == 400
        assert response.json()["error"]["type"] == "invalid_request_error"

    def test_count_tokens_forwarded_unbilled(self):
        response = self.post({"model": "claude-sonnet-test", "messages": [{"role": "user", "content": "hi"}]},
                             path="/v1/messages/count_tokens")
        assert response.status_code == 200
        assert response.json() == {"input_tokens": 42}
        assert str(self.upstream.requests[0].url) == "https://upstream.test/v1/messages/count_tokens"
        assert self.usage()["total_tokens"] == 0

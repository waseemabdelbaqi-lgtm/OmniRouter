"""
Anthropic Messages API pass-through (/v1/messages).

Lets Anthropic-native clients such as Claude Code use OmniRouter as their
ANTHROPIC_BASE_URL. Request bodies are forwarded to Anthropic unchanged (tools,
system prompts, content blocks, thinking, betas), and responses, including SSE
streams, are relayed byte-for-byte while token usage is recorded for the caller.
"""
import json
import os
from typing import Optional

import anyio
import httpx
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse, Response, StreamingResponse
from starlette.concurrency import run_in_threadpool

from serverRouter.core import config
from serverRouter.core.datamodels import ModelProvider
from serverRouter.core.models import MODELS
from serverRouter.routes.utils import validate_api_key, get_user_id_by_api_key, add_usage_to_user

router = APIRouter(prefix="/v1", tags=["messages"])

DEFAULT_ANTHROPIC_VERSION = "2023-06-01"
FORWARDED_REQUEST_HEADERS = ("anthropic-version", "anthropic-beta")
FORWARDED_RESPONSE_HEADERS = ("request-id", "retry-after", "anthropic-organization-id")
UPSTREAM_TIMEOUT = httpx.Timeout(connect=10.0, read=600.0, write=60.0, pool=10.0)

_upstream_client: Optional[httpx.AsyncClient] = None


def get_upstream_client() -> httpx.AsyncClient:
    """Shared HTTP client for calls to Anthropic."""
    global _upstream_client
    if _upstream_client is None:
        _upstream_client = httpx.AsyncClient(timeout=UPSTREAM_TIMEOUT)
    return _upstream_client


def anthropic_error(status_code: int, error_type: str, message: str) -> JSONResponse:
    """Error in the shape Anthropic clients expect."""
    return JSONResponse(
        status_code=status_code,
        content={"type": "error", "error": {"type": error_type, "message": message}},
    )


HTTP_STATUS_TO_ERROR_TYPE = {
    400: "invalid_request_error",
    401: "authentication_error",
    403: "permission_error",
    404: "not_found_error",
    429: "rate_limit_error",
}


def authenticate(request: Request) -> str:
    """Accept the OmniRouter key as x-api-key or Authorization: Bearer."""
    api_key = request.headers.get("x-api-key")
    if not api_key:
        auth = request.headers.get("authorization", "")
        scheme, _, token = auth.partition(" ")
        if scheme.lower() == "bearer":
            api_key = token.strip()
    if not api_key:
        raise HTTPException(status_code=401, detail="Missing API key")
    return validate_api_key(api_key)


def resolve_model(model: str) -> str:
    """Map OmniRouter aliases to Anthropic model IDs; pass real Claude IDs through."""
    model_info = MODELS.get(model)
    if model_info is None:
        return model
    if model_info.provider != ModelProvider.ANTHROPIC:
        raise HTTPException(
            status_code=400,
            detail=f"Model {model} is not an Anthropic model; /v1/messages only supports Anthropic models",
        )
    return model_info.name


def upstream_headers(request: Request, upstream_key: str) -> dict:
    headers = {
        "x-api-key": upstream_key,
        "content-type": "application/json",
        "anthropic-version": DEFAULT_ANTHROPIC_VERSION,
    }
    for name in FORWARDED_REQUEST_HEADERS:
        value = request.headers.get(name)
        if value:
            headers[name] = value
    return headers


def relay_headers(upstream: httpx.Response) -> dict:
    return {name: upstream.headers[name] for name in FORWARDED_RESPONSE_HEADERS if name in upstream.headers}


def usage_total(usage: dict) -> int:
    """Billable tokens in an Anthropic usage object, including cache reads/writes."""
    return sum(
        usage.get(field) or 0
        for field in ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")
    )


async def record_usage(user_id: str, token_count: int):
    if token_count > 0:
        await run_in_threadpool(add_usage_to_user, user_id, token_count)


async def prepare(request: Request):
    """Authenticate, parse the body and resolve the model. Returns (user_id, body, upstream_key)."""
    api_key = await run_in_threadpool(authenticate, request)
    user_id = await run_in_threadpool(get_user_id_by_api_key, api_key)

    try:
        body = await request.json()
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise HTTPException(status_code=400, detail="Request body must be valid JSON")
    if not isinstance(body, dict) or not isinstance(body.get("model"), str):
        raise HTTPException(status_code=400, detail="model: field required")
    body["model"] = resolve_model(body["model"])

    upstream_key = os.getenv("ANTHROPIC_API_KEY")
    if not upstream_key:
        raise HTTPException(status_code=500, detail="ANTHROPIC_API_KEY is not configured on the OmniRouter server")
    return user_id, body, upstream_key


@router.post("/messages")
async def create_message(request: Request):
    """Anthropic Messages API, streaming or not, forwarded to Anthropic."""
    try:
        user_id, body, upstream_key = await prepare(request)
    except HTTPException as e:
        return anthropic_error(e.status_code, HTTP_STATUS_TO_ERROR_TYPE.get(e.status_code, "api_error"), str(e.detail))

    client = get_upstream_client()
    upstream_request = client.build_request(
        "POST",
        f"{config.ANTHROPIC_UPSTREAM_URL}/v1/messages",
        headers=upstream_headers(request, upstream_key),
        content=json.dumps(body).encode(),
    )
    try:
        upstream = await client.send(upstream_request, stream=True)
    except httpx.HTTPError as e:
        return anthropic_error(502, "api_error", f"Could not reach Anthropic: {e}")

    is_stream = upstream.status_code == 200 and upstream.headers.get("content-type", "").startswith("text/event-stream")
    if not is_stream:
        content = await upstream.aread()
        await upstream.aclose()
        if upstream.status_code == 200:
            try:
                await record_usage(user_id, usage_total(json.loads(content).get("usage") or {}))
            except (json.JSONDecodeError, AttributeError):
                pass
        return Response(
            content=content,
            status_code=upstream.status_code,
            media_type=upstream.headers.get("content-type", "application/json"),
            headers=relay_headers(upstream),
        )

    usage = {}

    async def relay():
        buffer = b""
        try:
            async for chunk in upstream.aiter_bytes():
                yield chunk
                # Watch the stream for usage without altering it
                buffer += chunk
                *lines, buffer = buffer.split(b"\n")
                for line in lines:
                    if not line.startswith(b"data:"):
                        continue
                    try:
                        event = json.loads(line[5:])
                    except json.JSONDecodeError:
                        continue
                    if event.get("type") == "message_start":
                        usage.update((event.get("message") or {}).get("usage") or {})
                    elif event.get("type") == "message_delta":
                        # message_delta usage is cumulative, so later values replace earlier ones
                        usage.update({k: v for k, v in (event.get("usage") or {}).items() if v is not None})
        finally:
            # Runs on client disconnect too; shield so cleanup isn't cancelled with the stream
            with anyio.CancelScope(shield=True):
                await upstream.aclose()
                try:
                    await record_usage(user_id, usage_total(usage))
                except Exception as e:
                    print(f"Failed to record usage for {user_id}: {e}")

    return StreamingResponse(
        relay(),
        status_code=200,
        media_type="text/event-stream",
        headers={**relay_headers(upstream), "cache-control": "no-cache"},
    )


@router.post("/messages/count_tokens")
async def count_message_tokens(request: Request):
    """Anthropic token counting, forwarded to Anthropic. Not billed."""
    try:
        _, body, upstream_key = await prepare(request)
    except HTTPException as e:
        return anthropic_error(e.status_code, HTTP_STATUS_TO_ERROR_TYPE.get(e.status_code, "api_error"), str(e.detail))

    try:
        upstream = await get_upstream_client().post(
            f"{config.ANTHROPIC_UPSTREAM_URL}/v1/messages/count_tokens",
            headers=upstream_headers(request, upstream_key),
            content=json.dumps(body).encode(),
        )
    except httpx.HTTPError as e:
        return anthropic_error(502, "api_error", f"Could not reach Anthropic: {e}")

    return Response(
        content=upstream.content,
        status_code=upstream.status_code,
        media_type=upstream.headers.get("content-type", "application/json"),
        headers=relay_headers(upstream),
    )

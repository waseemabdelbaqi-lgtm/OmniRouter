# Using OmniRouter with Claude Code

OmniRouter exposes an Anthropic-compatible Messages API so Claude Code (and any other
Anthropic SDK client) can use it as its API endpoint. Requests are authenticated with an
OmniRouter key, forwarded to Anthropic unchanged, and billed to the key's user.

| Endpoint | Behavior |
|---|---|
| `POST /v1/messages` | Forwarded to Anthropic. Streaming (`"stream": true`) is relayed byte-for-byte. Usage is recorded. |
| `POST /v1/messages/count_tokens` | Forwarded to Anthropic. Not billed. |

Tools, system prompts, content blocks, extended thinking and prompt caching all pass through
untouched, and the client's `anthropic-version` and `anthropic-beta` headers are forwarded.
Only Anthropic models are supported on these endpoints. Real Claude model IDs are forwarded as-is,
and OmniRouter Claude aliases (e.g. `claude-3-5-haiku`) are mapped to their Anthropic IDs.

## Server setup

Set these in the server's environment or `.env` (never commit real values):

| Variable | Required | Purpose |
|---|---|---|
| `ANTHROPIC_API_KEY` | Yes | The server's own Anthropic key, used for all upstream calls. Clients never see it. |
| `OMNI_MAX_TOKENS` | Recommended | Per-user lifetime token limit (default `100000`). A Claude Code session uses tens of thousands of tokens per turn, so raise this. |
| `OMNI_ANTHROPIC_UPSTREAM_URL` | No | Upstream base URL (default `https://api.anthropic.com`). |

The server's other requirements are unchanged: `firebase-credentials.json` in the repo root and the
other provider keys (`OPENAI_API_KEY`, `GEMINI_API_KEY`, `TOGETHER_API_KEY`, `STABILITY_API_KEY`).

Do not set `ANTHROPIC_BASE_URL` in the server's environment. The Anthropic SDK used by the other
Claude routes reads it, and pointing it at OmniRouter would make the server call itself.

Start the server from the repo root:

```bash
uvicorn serverRouter.router:app --host 0.0.0.0 --port 8000
```

Each user needs an API key in Firestore: a document `api_keys/<key>` with `{"userid": "<user id>"}`,
and a document `users/<user id>` with `{"usage": {"total_tokens": 0, "total_messages": 0}}`.

## Client setup (Claude Code)

Point Claude Code at OmniRouter with environment variables:

```bash
export ANTHROPIC_BASE_URL="http://localhost:8000"   # OmniRouter's address, without /v1
export ANTHROPIC_AUTH_TOKEN="<your OmniRouter key>"
claude
```

Or persist them in `~/.claude/settings.json` (user-wide) or `.claude/settings.local.json` (per project):

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:8000",
    "ANTHROPIC_AUTH_TOKEN": "<your OmniRouter key>"
  }
}
```

`ANTHROPIC_API_KEY` also works on the client (sent as `x-api-key`), but in interactive mode Claude Code
asks you to approve a custom API key on first use; `ANTHROPIC_AUTH_TOKEN` avoids that prompt.

Optional client settings:

| Variable | Purpose |
|---|---|
| `ANTHROPIC_MODEL` | Model for the main loop, e.g. `claude-sonnet-4-5` |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | Model for background tasks |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` | Disables telemetry and other background traffic |

## Troubleshooting

- **Claude Code hangs or keeps retrying:** check the server log. Repeated `401 Unauthorized` means
  the OmniRouter key is wrong (Claude Code retries auth errors from a gateway rather than exiting).
  `429` means the user reached `OMNI_MAX_TOKENS`.
- **`500 ANTHROPIC_API_KEY is not configured`:** the server has no upstream key.
- **`400 ... is not an Anthropic model`:** `ANTHROPIC_MODEL` is set to a non-Claude OmniRouter model.

## Testing

`python -m pytest testLib/test_messages.py -v` runs offline, with Firestore and the Anthropic API
replaced by fakes.

"""Shared configuration constants for the OmniLLM API."""
import os
import firebase_admin
from firebase_admin import credentials, firestore

# Service-account key file; never commit it (see firebase-credentials.example.json)
cred = credentials.Certificate(os.getenv("FIREBASE_CREDENTIALS_PATH", "firebase-credentials.json"))
app = firebase_admin.initialize_app(cred)
db = firestore.client()
VALID_API_KEYS = set()

def update_api_keys(keys_snapshot, changes, read_time):
    """Update the VALID_API_KEYS set when changes occur in Firestore."""
    global VALID_API_KEYS
    VALID_API_KEYS = {key.id for key in keys_snapshot}

initial_keys = db.collection('api_keys').get()
update_api_keys(initial_keys, None, None)
api_keys_watch = db.collection('api_keys').on_snapshot(update_api_keys)

PROVIDERS = {}
# Per-user lifetime token limit; Claude Code sessions need far more than the default
MAX_TOKENS = int(os.getenv("OMNI_MAX_TOKENS", "100000"))

# Upstream for the /v1/messages pass-through. Deliberately not ANTHROPIC_BASE_URL,
# which clients set to point at OmniRouter itself.
ANTHROPIC_UPSTREAM_URL = os.getenv("OMNI_ANTHROPIC_UPSTREAM_URL", "https://api.anthropic.com").rstrip("/")

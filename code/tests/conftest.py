"""Shared test setup.

The day scripts build an Anthropic client when they are imported, and the client
needs an API key. A fake key lets them import, and it means any test that
reached the real API by mistake would fail on authentication instead of
spending money. No test here calls the API.
"""

import os

os.environ["ANTHROPIC_API_KEY"] = "test-key-not-real"

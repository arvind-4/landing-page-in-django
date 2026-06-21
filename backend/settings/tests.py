"""Test settings that override local for testing."""

import tempfile
from pathlib import Path

from backend.settings.local import *
from backend.settings.local import BASE_DIR

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_ROOT = Path(tempfile.mkdtemp())

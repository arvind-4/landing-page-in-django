"""Production settings."""

import os

from backend.settings.base import *
from backend.settings.base import BASE_DIR

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = os.environ.get("DJANGO_DEBUG")

ALLOWED_HOSTS = ["*"]

ADMIN_URL = os.environ.get("DJANGO_ADMIN_URL")

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles_build" / "static"

"""Local development settings."""

from backend.env_utils import get_env_as_bool, get_env_as_list, get_env_as_str
from backend.settings.base import *
from backend.settings.base import BASE_DIR

SECRET_KEY = get_env_as_str(key="DJANGO_SECRET_KEY")

DEBUG = get_env_as_bool(key="DJANGO_DEBUG")

ALLOWED_HOSTS = get_env_as_list(key="DJANGO_ALLOWED_HOSTS")

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles_build" / "static"

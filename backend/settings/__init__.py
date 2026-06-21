"""Settings package."""

from backend.env_utils import get_env_as_bool

DJANGO_LIVE = get_env_as_bool(key="DJANGO_LIVE")
CI = get_env_as_bool(key="CI")

if CI:
    from backend.settings.tests import *
elif DJANGO_LIVE:
    from backend.settings.production import *
else:
    from backend.settings.local import *

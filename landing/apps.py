"""App configuration for the landing app."""

from django.apps import AppConfig
from django.utils.functional import cached_property


class LandingConfig(AppConfig):
    """Configuration for the landing app."""

    @cached_property
    def default_auto_field(self) -> str:
        """Return the default auto field for models."""
        return "django.db.models.BigAutoField"

    name = "landing"

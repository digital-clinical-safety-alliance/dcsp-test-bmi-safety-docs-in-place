from django.apps import AppConfig


class AppConfig(AppConfig):  # type: ignore[no-redef]
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"

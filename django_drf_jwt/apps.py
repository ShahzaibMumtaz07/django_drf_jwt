from django.apps import AppConfig


class DjangoDrfJwtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_drf_jwt'
    from django_drf_jwt.settings import *

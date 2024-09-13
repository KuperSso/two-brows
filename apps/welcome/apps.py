from django.apps import AppConfig


class WelcomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.welcome'
    verbose_name = "Главная страница и Дипломы"
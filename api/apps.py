from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        from .signals import update_account, update_credit

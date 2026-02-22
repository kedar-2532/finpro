from django.apps import AppConfig


class RiskConfig(AppConfig):
    name = 'apps.risk'

    def ready(self):
        import apps.risk.signals
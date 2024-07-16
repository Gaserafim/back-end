from django.apps import AppConfig


class HqsConfig(AppConfig):
    name = 'hqs'

    def ready(self):
        import hqs.signals

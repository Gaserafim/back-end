from django.apps import AppConfig


class SoundsConfig(AppConfig):
    name = 'sounds'

    def ready(self):
        import sounds.signals
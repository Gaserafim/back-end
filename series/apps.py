from django.apps import AppConfig


class SeriesConfig(AppConfig):
    name = 'series'

    def ready(self):
        import series.signals
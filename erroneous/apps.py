from django.apps import AppConfig


class ErroneousConfig(AppConfig):
    name = "erroneous"

    def ready(self):
        import erroneous.signals

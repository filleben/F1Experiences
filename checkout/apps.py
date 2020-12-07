from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Import checkout singals
    """
    name = 'checkout'

    def ready(self):
        import checkout.signals

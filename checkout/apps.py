from django.apps import AppConfig

#Import checkout singals
class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals

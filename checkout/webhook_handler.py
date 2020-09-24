from django.http import HttpResponse

class StripeWebhook_Handler:
    """
    Handle webhooks sent from stripe
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle any generic/unknown or unexpected webhook events
        """
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment_intent.succeeded webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle payment_intent.payment_failed webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200
        )
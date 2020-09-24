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
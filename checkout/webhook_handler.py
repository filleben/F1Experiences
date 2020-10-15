from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderLineItem
from races.models import Ticket
from accounts.models import UserProfile
import json
import time

class StripeWebhook_Handler:
    """
    Handle webhooks sent from stripe
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        customer_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_number': settings.DEFAULT_CONTACT_NUMBER})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

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
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        order_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = billing_details.phone
                profile.default_street_address1 = billing_details.address.line1
                profile.default_street_address2 = billing_details.address.line2
                profile.default_town_or_city = billing_details.address.city
                profile.default_county = billing_details.address.state
                profile.default_country = billing_details.address.country
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    town_or_city__iexact=billing_details.address.city,
                    county__iexact=billing_details.address.state,
                    country__iexact=billing_details.address.country,
                    order_total=order_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook Received: {event["type"]} | SUCCESS: Order has been created',
                status=200
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    town_or_city=billing_details.address.city,
                    county=billing_details.address.state,
                    country=billing_details.address.country,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    ticket = Ticket.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        ticket=ticket,
                        quantity=item_data,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook Received: {event["type"]} | ERROR: {e}',
                    status=500
                )
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook Received: {event["type"]} | SUCCESS: Order created in webhook',
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
from django.shortcuts import render, redirect , reverse
from django.contrib import messages
from .forms import OrderForm
from django.conf import settings
from cart.contexts import cart_contents
from races.models import Race, Ticket
from .models import OrderLineItem
import stripe

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                ticket = Ticket.objects.get(id=item_id)
                order_line_item = OrderLineItem(
                    order=order,
                    ticket=ticket,
                    quantity=item_data,
                )
                order_line_item.save()

            return redirect(reverse('checkout_success', args=[order.order_number]))

        else:
            messages.error(request, "Sorry there was a problem, please check the information you have provided")

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is empty")
            return redirect(reverse('races'))

        current_cart = cart_contents(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency='gbp',
        )

        print(intent)

        order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render (request, 'checkout/checkout.html', context)
from django.shortcuts import render, redirect , reverse
from django.contrib import messages
from .forms import OrderForm
from django.conf import settings

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('races'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }

    return render (request, 'checkout/checkout.html', context)
from django.shortcuts import render, redirect , reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('races'))

    order_form = OrderForm()
    context = {
        'order_form': order_form
    }

    return render (request, 'checkout/checkout.html', context)
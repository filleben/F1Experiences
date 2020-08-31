from django.shortcuts import render, redirect, reverse
from races.models import Ticket

# Create your views here.

def view_cart(request):
    return render(request, 'cart/cart.html')

def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(reverse('view_cart'))
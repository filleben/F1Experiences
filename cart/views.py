from django.shortcuts import render, redirect, reverse
from races.models import Ticket

#View Cart
def view_cart(request):
    return render(request, 'cart/cart.html')

#Add to Cart
def add_to_cart(request, id):
    """
    Gets the item quantity and adds it to the cart
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    
    return redirect(reverse('view_cart'))

#Remove from Cart
def remove_item(request, id):
    """
    Removes item from the cart
    """
    cart = request.session.get('cart', {})
    quantity = cart[id] - 1

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    
    return redirect(reverse('view_cart'))
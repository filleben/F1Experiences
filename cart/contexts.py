from django.shortcuts import get_object_or_404
from races.models import Ticket

def cart_contents(request):

    cart_items = []
    total = 0
    ticket_count = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'ticket_count': ticket_count,
    }

    return context
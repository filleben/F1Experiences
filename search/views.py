from django.shortcuts import render
from races.models import Race, Ticket

# Create your views here.

def search(request):
    if request.method == "GET":
        races = Race.objects.filter(friendly_name__icontains=request.GET['q'])
        context = {
            'races': races
        }
        return render(request, 'races/races.html', context)

def ticket_search(request):
    if request.method == "GET":
        tickets = Ticket.objects.filter(name__icontains=request.GET['q'])
        context = {
            'tickets': tickets
        }
        return render(request, 'races/ticket_management.html', context)
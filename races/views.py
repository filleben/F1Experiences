from django.shortcuts import render
from .models import Race, Ticket

# Create your views here.

def all_races(request):
    races = Race.objects.all()
    context = {
        'races': races,
    }
    return render(request, 'races/races.html', context)

def race_details(request, race_id):
    races = Race.objects.filter(id=race_id)
    tickets = Ticket.objects.filter(race_id=race_id)

    if not Race.objects.exists():
        raise Http404

    context = {
        'races': races,
        'tickets': tickets,
    }
    return render(request, 'races/race_details.html', context)
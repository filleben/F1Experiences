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

    race_object=Race.objects.get(id=race_id)
    race_object.race_views=race_object.race_views+1
    race_object.save()

    if not Race.objects.exists():
        raise Http404

    context = {
        'races': races,
        'tickets': tickets,
    }
    return render(request, 'races/race_details.html', context)
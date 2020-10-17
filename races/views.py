from django.shortcuts import render
from .models import Race, Ticket
from .forms import RaceForm, TicketForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def all_races(request):
    race_list = Race.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(race_list, 6)
    try:
        races = paginator.page(page)
    except PageNotAnInteger:
        races = paginator.page(1)
    except EmptyPage:
        races = paginator.page(paginator.num_pages)

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

def add_race(request):
    form = RaceForm()
    context = {
        'form': form,
    }

    return render(request, 'races/add_race.html', context)

def add_ticket(request):
    form = TicketForm()
    context = {
        'form': form,
    }

    return render(request, 'races/add_ticket.html', context)
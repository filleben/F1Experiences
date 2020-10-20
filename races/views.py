from django.shortcuts import render, redirect, reverse
from django.contrib import messages
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
    if request.method == 'POST':
        form = RaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added new race event!')
            return redirect(reverse('add_race'))
        else:
            messages.error(request, 'Error adding race event, please check your form and try again.')
    else:
        form = RaceForm()
    context = {
        'form': form,
    }

    return render(request, 'races/add_race.html', context)

def add_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added new ticket!')
            return redirect(reverse('add_ticket'))
        else:
            messages.error(request, 'Error adding ticket, please check your form and try again.')
    else:
        form = TicketForm()
    context = {
        'form': form,
    }

    return render(request, 'races/add_ticket.html', context)
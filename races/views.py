from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

@login_required
def event_management(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))
    
    races = Race.objects.all()
    context = {
        'races': races,
    }
    return render(request, 'races/event_management.html', context)

@login_required
def ticket_management(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))
    
    tickets = Ticket.objects.all()
    context = {
        'tickets': tickets,
    }
    return render(request, 'races/ticket_management.html', context)

@login_required
def add_race(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

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

@login_required
def add_ticket(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

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

@login_required
def edit_race(request, race_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    race = get_object_or_404(Race, pk=race_id)
    if request.method == 'POST':
        form = RaceForm(request.POST, request.FILES, instance=race)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated race event!')
            return redirect(reverse('race_detail', args=[race.id]))
        else:
            messages.error(request, 'Error editing race event, please check your form and try again.')
    else:
        form = RaceForm(instance=race)
    context = {
        'form': form,
        'race': race,
    }

    return render(request, 'races/edit_race.html', context)

@login_required
def delete_race(request, race_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    race = get_object_or_404(Race, pk=race_id)
    race.delete()
    messages.success(request, 'Successfully deleted race event!')
    return redirect(reverse('event_management'))

@login_required
def edit_ticket(request, ticket_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    tickets = Ticket.objects.filter(id=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=tickets)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added new ticket!')
            return redirect(reverse('ticket_management'))
        else:
            messages.error(request, 'Error adding ticket, please check your form and try again.')
    else:
        form = TicketForm(instance=tickets)
    context = {
        'form': form,
        'tickets': tickets,
    }

    return render(request, 'races/edit_ticket.html', context)

@login_required
def delete_ticket(request, ticket_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))
        
    tickets = Ticket.objects.filter(id=ticket_id)
    ticket.delete()
    messages.success(request, 'Successfully deleted ticket!')
    return redirect(reverse('ticket_management'))
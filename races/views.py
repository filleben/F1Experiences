from django.shortcuts import render
from .models import Race

# Create your views here.

def all_races(request):
    races = Race.objects.all()
    context = {
        'races': races,
    }
    return render(request, 'races/races.html', context)
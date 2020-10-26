from django.shortcuts import render
from races.models import Race

# Create your views here.

def popular_races(request):
    races = Race.objects.order_by('-race_views')[:4]

    context = {
        'races': races,
    }
    return render(request, 'home/index.html', context)

def handler_404(request, exception):
    return render(request, '404.html')
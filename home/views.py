from django.shortcuts import render
from races.models import Race

#Most Popular Races
def popular_races(request):
    """
    Displays the 4 most popular race events
    """
    races = Race.objects.order_by('-race_views')[:4]

    context = {
        'races': races,
    }
    return render(request, 'home/index.html', context)

#404 error handler
def handler_404(request, exception):
    return render(request, '404.html')
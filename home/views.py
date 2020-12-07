from django.shortcuts import render
from races.models import Race


def popular_races(request):
    """
    Displays the 4 most popular race events
    """
    races = Race.objects.order_by('-race_views')[:4]

    context = {
        'races': races,
    }
    return render(request, 'home/index.html', context)


def handler_404(request, exception):
    """
    404 Error Handler
    """
    return render(request, '404.html')

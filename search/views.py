from django.shortcuts import render
from races.models import Race

# Create your views here.

def search(request):
    if request.method == "GET":
        races = Race.objects.filter(friendly_name__icontains=request.GET['q'])
        context = {
            'races': races
        }
        return render(request, 'races/races.html', context)
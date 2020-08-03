from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_races, name='races'),
    path('<race_id>', views.race_details, name='race_detail'),
]

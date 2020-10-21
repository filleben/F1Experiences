from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_races, name='races'),
    path('<int:race_id>/', views.race_details, name='race_detail'),
    path('add_race/', views.add_race, name='add_race'),
    path('add_ticket/', views.add_ticket, name='add_ticket'),
    path('edit_race/<int:race_id>/', views.edit_race, name='edit_race'),
]

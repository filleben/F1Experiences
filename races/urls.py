from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_races, name='races'),
    path('<int:race_id>/', views.race_details, name='race_detail'),
    path('add_race/', views.add_race, name='add_race'),
    path('add_ticket/', views.add_ticket, name='add_ticket'),
    path('edit_race/<int:race_id>/', views.edit_race, name='edit_race'),
    path('delete_race/<int:race_id>/', views.delete_race, name='delete_race'),
    path('edit_ticket/<int:ticket_id>/',
         views.edit_ticket,
         name='edit_ticket'),
    path('delete_ticket/<int:ticket_id>/',
         views.delete_ticket,
         name='delete_ticket'),
    path('event_management/',
         views.event_management,
         name='event_management'),
    path('ticket_management/',
         views.ticket_management,
         name='ticket_management'),
]

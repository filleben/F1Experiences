from django.urls import path
from . import views

urlpatterns = [
    path('races/', views.event_search, name='event_search'),
    path('ticket_management/',
         views.ticket_management_search,
         name='ticket_management_search'),
    path('event_management/',
         views.event_management_search,
         name='event_management_search'),
]

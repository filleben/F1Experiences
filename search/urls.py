from django.urls import path
from . import views

urlpatterns = [
    path('races/', views.search, name='search'),
    path('ticket_management/', views.ticket_search, name='ticket_search'),
]

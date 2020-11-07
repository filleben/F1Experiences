from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact_success/<contact_number>', views.contact_success, name='contact_success'),
]

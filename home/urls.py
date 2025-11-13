from django.urls import path
from .views import home

urls = [
    path('', home, name='home'),
]

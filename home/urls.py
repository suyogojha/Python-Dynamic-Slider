
from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name='home'),    
    path('api/hotels', api_hotels),    
]

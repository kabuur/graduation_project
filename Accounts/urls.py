
from django.urls import path
from .views import Regestration

urlpatterns  = [
   
    path('Regestration/', Regestration, name='Regestration'),
    # path('login', Login, name='home'),
]
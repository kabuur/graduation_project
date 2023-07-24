
from django.urls import path
from .views import pateintUser

urlpatterns  = [
   
    path('pateintUser/', pateintUser, name='pateintUser'),

]

from django.urls import path
from .views import Regestration,chooseAccount,loginIndivitual,predictIndivitual

urlpatterns  = [
   
    path('Regestration/', Regestration, name='Regestration'),
    
     path('loginIndivitual/', loginIndivitual, name='loginIndivitual'),
    path('chooseAccount/', chooseAccount, name='chooseAccount'),
    path('predictIndivitual/', predictIndivitual, name='predictIndivitual'),

]
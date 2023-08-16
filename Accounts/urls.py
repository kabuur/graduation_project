
from django.urls import path
from .views import Regestration,chooseAccount,loginIndivitual,predictIndivitual,registerIndivitual

urlpatterns  = [
   
    path('Regestration/', Regestration, name='Regestration'),
    
     path('loginIndivitual/', loginIndivitual, name='loginIndivitual'),
     path('registerIndivitual/', registerIndivitual, name='registerIndivitual'),
    path('chooseAccount/', chooseAccount, name='chooseAccount'),
    path('predictIndivitual/', predictIndivitual, name='predictIndivitual'),

]
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Hospital
# Create your views here.



def Regestration(Request):
    massage = ""
    if Request.method == "POST":
        userName = Request.POST.get('userName')
        hospName = Request.POST.get('hospName')
        email = Request.POST.get('email')
        tell = Request.POST.get('tell')
        password1 = Request.POST.get('password1') 
        password2 = Request.POST.get('password2') 
        address = Request.POST.get('address')
        
        if password1!= password2:
             massage = "password must be same"
             
        else:
            my_user = User.objects.create_user(username = userName, password=password1)
            my_user.save()
            
            user = User.objects.get(username =userName )
            
            print(user)
            
            hospital = Hospital.objects.create(
                    HospitalName = hospName,
                    userName = user,
                    tell = tell,
                    email = email,
                    address  = address
                    
            )
            hospital.save()
            return HttpResponse("created")
  
    return render(Request, 'registration/reg.html',{"massage": massage},)

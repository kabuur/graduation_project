from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
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
        
        if password1!= password2:
             massage = "password must be same"
             
        else:
            my_user = User.objects.create_user(username = userName, password=password1,email = email, first_name = hospName,last_name=tell)
            my_user.save()
            return HttpResponse("created")
  
    return render(Request, 'files/reg.html',{"massage": massage},)

def Login(Request):
    return 
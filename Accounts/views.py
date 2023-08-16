from pyexpat.errors import messages
import warnings
from PIL import Image, ImageEnhance
warnings.filterwarnings('ignore')
import tensorflow as tf
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np
#from keras.preprocessing import image
import keras.utils as image
import os
from django.core.files.storage import FileSystemStorage


from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Hospital,IndivitualUser
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
        if(User.objects.filter(username = userName)):
                massage = "this user name "+ userName+ " is allready exist"
                return render(Request, 'registration/reg.html',{"massage": massage},)
        if password1!= password2:
             massage = "password must be same"
             return render(Request, 'registration/reg.html',{"massage": massage},)
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
                return redirect('/login')
  
    return render(Request, 'registration/reg.html',{"massage": massage},)




def chooseAccount(Request):
        return render(Request,"registration/Accounts.html")


def loginIndivitual(Request):
        
        if Request.method == "POST":
                userName = Request.POST.get("userName")
                Password = Request.POST.get("Password")
              
                if IndivitualUser.objects.filter(userName = userName , password = Password):
                        # return render (Request,"registration/predictIndivitual.html")
                        return redirect('/predictIndivitual')
                else:
                        context= {
                                "message":"Please enter a correct username and password. Note that both fields may be case-sensitive."
                        }
                        return render(Request,"registration/loginIndivitual.html",context) 
        return render(Request,"registration/loginIndivitual.html")


def registerIndivitual(Request):
        if Request.method == "POST":
                name = Request.POST.get("name")
                tell  = Request.POST.get("tell")
                userName = Request.POST.get("userName")
                password1 = Request.POST.get("Password1")
                password2 = Request.POST.get("Password2")
                if IndivitualUser.objects.filter(userName =userName):
                        context = {
                                "message":"this user name "+ userName +" is already exist"
                        }
                        return render(Request,"registration/registerIndivitual.html",context)
                else:
                        
                        if (password1 == password2):
                                
                                create = IndivitualUser.objects.create(
                                userName = userName,
                                password = password1,
                                tell =tell,
                                name = name,
                                )
                                create.save()
                                return redirect("/loginIndivitual")
                        else:
                                context = {
                                        "message":"Password Must be Same"
                                }
                                return render(Request,"registration/registerIndivitual.html",context)

                        
                
        
        return render(Request,"registration/registerIndivitual.html")

# @login_required(login_url='/loginIndivitual')
def predictIndivitual(Request):
        if Request.method == "POST":
                
                output=""
                img_file = Request.FILES['xrayImage']
                testType = Request.POST.get('testType')
               
                fs = FileSystemStorage()
                
                filename = fs.save('./indivitual/'+img_file.name, img_file)
                path = "./media/"+filename
                img = "/media/"+filename
                
               
            
              
                
                path=str(path)
                print(path)
                if testType == 'TUBERCULOSIS':
                        model=load_model('./TB.h5')
                else:
                        model=load_model('./PN.h5')
                
                img_file=image.load_img(path,target_size=(224,224))
                x=image.img_to_array(img_file)
                x=np.expand_dims(x, axis=0)
                img_data=preprocess_input(x)
                classes=model.predict(img_data)
                global result
                result=classes
                print(result[0][0])
                if testType == 'TUBERCULOSIS':
                        if result[0][0]>0.5:
                                output = "Result is Normal"
                                print("Result is Normal")
                        else:                    
                                output = "effected by Tuberclusis"
                                print("effected by Tuberclusis")
                else:
                        if result[0][0]>0.5:
                                output = "Result is Normal"
                                print("Result is Normal")
                        else:                    
                                output = "effected by Pnemonia"
                                print("effected by Pnemonia")
                contex = {
                        "output":output,
                        "img":img
                }
                return render (Request,"registration/predictIndivitual.html",contex)
                
        return render (Request,"registration/predictIndivitual.html")
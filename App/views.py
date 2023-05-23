# from django.shortcuts import render
# from django.http import HttpRequest,HttpResponse
# from django.shortcuts import render
# # Create your views here.


# def Home(Request):
#     return render(Request ,'App/index.html')

import warnings
from PIL import Image, ImageEnhance
warnings.filterwarnings('ignore')
import tensorflow as tf
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np
#from keras.preprocessing import image
import keras.utils as image



from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# from .models import members
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import  Patient,NormalPN,NormalTB,Tuberculosis,Pneumonia
from django.contrib.auth.models import User








def  Home(Request):
    
    output = ''
    global pat 
    id = ''
    global imag
    
    if(Request.method == "POST"):
      
        if Request.POST.get('ID'):
            
           #geting patient
            username = Request.user.username
            
            pat = Patient.objects.filter(patientID =  Request.POST.get("ID"),userName=User.objects.get(username = username)).values()
            if(len(pat) == 0):
                 person = "ma ahan mid jiro shiqsigaan"
                 context= {
                     "person": person
                 }
                 return render(Request,"App/index.html",context)
            imag = './media/'+pat[0]['patientXrayImage']
            id = pat[0]['patientID']
        
        
        elif(Request.POST.get('pridicts')):
            
            path=imag
            path=str(path)
            print(path)
            
            if pat[0]['testType'] == 'TUBERCULOSIS':
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
            
            print( ( result[0][0]))
            
            if pat[0]['testType'] == 'TUBERCULOSIS':
                if result[0][0]>0.5:
                    output = "Result is Normal"
                    print("Result is Normal")
                    id =   pat[0]['patientID']
                    normal =  NormalTB.objects.filter(patientID = id).values()
                 
                    length = len(normal)
                    if (length != 1):
                        normal = NormalTB(
                                userName =  pat[0]['UserName'] ,
                                patientID = pat[0]['patientID'] ,
                                patientName = pat[0]['patientName'] ,
                                patientTell =pat[0]['patientTell'] ,
                                paientAge = pat[0]['paientAge'] ,
                                pridected = pat[0]['testType'] ,
                                patientGenter = pat[0]['patientGenter'] ,
                                patientAddress = pat[0]['patientAddress'] ,
                                patientRegDate = pat[0]['patientRegDate'] ,
                                patientXrayImage = pat[0]['patientXrayImage'] ,
                        )
                        normal.save()
                else:
                   
                    output = "Affected By Tubarculosis"
                    print("Affected By Tubarculosis")
                    
                    id =   pat[0]['patientID']
                    TB =  Tuberculosis.objects.filter(patientID = id).values()
                 
                    length = len(TB)
                    if (length != 1):
                        TB = Tuberculosis(
                                userName =  pat[0]['userName_id'] ,
                                patientID = pat[0]['patientID'] ,
                                patientName = pat[0]['patientName'] ,
                                patientTell =pat[0]['patientTell'] ,
                                paientAge = pat[0]['paientAge'] ,
                                pridected = pat[0]['testType'] ,
                                patientGenter = pat[0]['patientGenter'] ,
                                patientAddress = pat[0]['patientAddress'] ,
                                patientRegDate = pat[0]['patientRegDate'] ,
                                patientXrayImage = pat[0]['patientXrayImage'] ,
                        )
                        TB.save()
                   
            else:
                if result[0][0]>0.5:
                    output = "Result is Normal"
                    print("Result is Normal")
                    id =   pat[0]['patientID']
                    pn =  NormalPN.objects.filter(patientID = id).values()
                 
                    length = len(pn)
                    if (length != 1):
                            normal = NormalPN(
                                    userName =  pat[0]['userName_id'] ,
                                    patientID = pat[0]['patientID'] ,
                                    patientName = pat[0]['patientName'] ,
                                    patientTell =pat[0]['patientTell'] ,
                                    paientAge = pat[0]['paientAge'] ,
                                    pridected = pat[0]['testType'] ,
                                    patientGenter = pat[0]['patientGenter'] ,
                                    patientAddress = pat[0]['patientAddress'] ,
                                    patientRegDate = pat[0]['patientRegDate'] ,
                                    patientXrayImage = 'TB/Tuberculosis/'+pat[0]['patientXrayImage'] 
                            )
                            normal.save()
                    
                else:
                    output = "Affected By PNEUMONIA"
                    print("Affected By PNEUMONIA")
                    id =   pat[0]['patientID']
                    pn =  Pneumonia.objects.filter(patientID = id).values()
                 
                    length = len(pn)
                    if (length != 1):
                            PN = Pneumonia(
                                    userName =  pat[0]['userName_id'] ,
                                    patientID = pat[0]['patientID'] ,
                                    patientName = pat[0]['patientName'] ,
                                    patientTell =pat[0]['patientTell'] ,
                                    paientAge = pat[0]['paientAge'] ,
                                    pridected = pat[0]['testType'] ,
                                    patientGenter = pat[0]['patientGenter'] ,
                                    patientAddress = pat[0]['patientAddress'] ,
                                    patientRegDate = pat[0]['patientRegDate'] ,
                                    patientXrayImage = 'TB/Tuberculosis/'+pat[0]['patientXrayImage'] 
                            )
                            PN.save()
        else:
             return render(Request,"App/index.html")
            

        
        context = {
            "patient" : pat,
            "imag" : imag,
            "output": output,
            "id": id
        
        }
        return render(Request,"App/index.html",context)
    
       
        
    else:
        return render(Request,"App/index.html")


def X_Rey(Request):
    if Request.method == 'POST':
        name = Request.POST.get('name')
        id = Request.POST.get('id')
        tell = Request.POST.get('tell')
        age = Request.POST.get('age')
        gender = Request.POST.get('gender')
        address = Request.POST.get('address')
        test = Request.POST.get('type')
        xrayImage = Request.FILES['xrayImage']
      
        username = Request.user.username
       
        print(username)
        
   
        
        pat = Patient(
                patientID = id,
                patientName = name,
                patientTell = tell,
                paientAge = age,
                testType = test,
                patientGenter = gender,
                patientAddress = address,
                patientXrayImage = xrayImage,
                userName = User.objects.get(username = username)
        )
        pat.save()
        
        
        # img_file = Request.FILES['X_ray']
        # fs = FileSystemStorage()
        # filename = fs.save('./xray/'+img_file.name, img_file)
        # print(filename)
    return render(Request ,'App/patient.html')




   

   

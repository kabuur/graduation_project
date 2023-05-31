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
from .models import  Patient,TuberculosisTests,PneumoniaTests
from django.contrib.auth.models import User
from datetime import datetime




def TBPridicted():
    TBPridicted =  Patient.objects.filter(pridected = 'TUBERCULOSIS').values
    # Patient.objects.raw( "SELECT ID ,SUM()")
    
    return TBPridicted


def notPridicted():
    notPridicted =  Patient.objects.filter(isPridicted = False).values
    
    return notPridicted

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
                     "person": person,
                     "notPridicted": notPridicted()
                 }
                 return render(Request,"App/index.html",context)
            imag = './media/'+pat[0]['patientXrayImage']
            id = pat[0]['patientID']
        
        
        elif(Request.POST.get('pridicts')):
            isPridictedUpdate = Patient.objects.get(patientID=pat[0]['patientID'])
            isPridictedUpdate.isPridicted = True
            isPridictedUpdate.save()
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
                    TB =  TuberculosisTests.objects.filter(patientID = id).values()
                 
                    length = len(TB)
                    if (length != 1):
                        TB = TuberculosisTests(
                                userName =  pat[0]['userName_id'] ,
                                patientID = pat[0]['patientID'] ,
                                patientName = pat[0]['patientName'] ,
                                patientTell =pat[0]['patientTell'] ,
                                paientAge = pat[0]['paientAge'] ,
                                pridected = 'Normal' ,
                                patientGenter = pat[0]['patientGenter'] ,
                                patientAddress = pat[0]['patientAddress'] ,
                                patientRegDate = pat[0]['patientRegDate'] ,
                                patientXrayImage = pat[0]['patientXrayImage'] ,
                        )
                        TB.save()
                else:
                   
                    output = "Affected By Tubarculosis"
                    print("Affected By Tubarculosis")
                    
                    id =   pat[0]['patientID']
                    TB =  TuberculosisTests.objects.filter(patientID = id).values()
                 
                    length = len(TB)
                    if (length != 1):
                        TB = TuberculosisTests(
                                userName =  pat[0]['userName_id'] ,
                                patientID = pat[0]['patientID'] ,
                                patientName = pat[0]['patientName'] ,
                                patientTell =pat[0]['patientTell'] ,
                                paientAge = pat[0]['paientAge'] ,
                                pridected = 'TUBERCULOSIS' ,
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
                    pn =  PneumoniaTests.objects.filter(patientID = id).values()
                 
                    length = len(pn)
                    if (length != 1):
                            PN = PneumoniaTests(
                                    userName =  pat[0]['userName_id'] ,
                                    patientID = pat[0]['patientID'] ,
                                    patientName = pat[0]['patientName'] ,
                                    patientTell =pat[0]['patientTell'] ,
                                    paientAge = pat[0]['paientAge'] ,
                                    pridected = 'PNEUMONIA' ,
                                    patientGenter = pat[0]['patientGenter'] ,
                                    patientAddress = pat[0]['patientAddress'] ,
                                    patientRegDate = pat[0]['patientRegDate'] ,
                                    patientXrayImage = 'TB/Tuberculosis/'+pat[0]['patientXrayImage'] 
                            )
                            PN.save()
                    
                else:
                    output = "Affected By PNEUMONIA"
                    print("Affected By PNEUMONIA")
                    id =   pat[0]['patientID']
                    pn =  PneumoniaTests.objects.filter(patientID = id).values()
                 
                    length = len(pn)
                    if (length != 1):
                            PN = PneumoniaTests(
                                    userName =  pat[0]['userName_id'] ,
                                    patientID = pat[0]['patientID'] ,
                                    patientName = pat[0]['patientName'] ,
                                    patientTell =pat[0]['patientTell'] ,
                                    paientAge = pat[0]['paientAge'] ,
                                    pridected = 'Normal' ,
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
      
        context = {
          
            "notPridicted": notPridicted()
        }
     
        return render(Request,"App/index.html",context)


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




   
def dashboard (Request):
   
    #TB chart
    TBresults = []
    countTBresults = []
    username = Request.user.username
    user = User.objects.get(username = username)
    id =  user.id
    for resalts in TuberculosisTests.objects.raw( "SELECT ID,  COUNT(patientID)count ,pridected,userName FROM App_TuberculosisTests  GROUP BY pridected"):
        
        if(resalts.userName == id):
            
            TBresults.append(resalts.pridected)
            countTBresults.append(resalts.count)
    #PN chart
    PNresults = []
    countPNresults = []
    username = Request.user.username
    user = User.objects.get(username = username)
   
    for resalts in PneumoniaTests.objects.raw( "SELECT ID,  COUNT(patientID)count ,pridected,userName FROM App_PneumoniaTests  GROUP BY pridected"):
        
        if(resalts.userName == id):
          
            PNresults.append(resalts.pridected)
            countPNresults.append(resalts.count)
    
    
    #Main chart
    RegisterYear_monthCount = []
    countRegister = []  
    for results in Patient.objects.raw( "SELECT ID, userName_id ,COUNT(patientID)count,strftime('%Y-%m', patientRegDate) year_month FROM App_Patient GROUP BY year_month  "):
        
       
       
        if (results.userName_id == id):
            countRegister.append(results.count)
            RegisterYear_monthCount.append(results.year_month)
    
    
    
    countTB = len(TuberculosisTests.objects.filter(userName = id,pridected = 'TUBERCULOSIS').values())
    countNormalLtb = len(TuberculosisTests.objects.filter(userName = id,pridected = 'Normal').values())
    countPN = len(PneumoniaTests.objects.filter(userName = id,pridected = 'PNEUMONIA').values())
    countNormalPN = len(PneumoniaTests.objects.filter(userName = id,pridected = 'Normal').values())

    
    
    
    
    
    
    
    context = {
        
        
        "countTB": countTB,
        "countNormalLtb":countNormalLtb,
        "countNormalPN":countNormalPN,
        "countPN": countPN,
        
        
        'PNresults':PNresults,
        'countPNresults':countPNresults,
        'TBresults':TBresults,
        
        'countTBresults':countTBresults,
        'RegisterYear_monthCount':RegisterYear_monthCount,
        'countRegister':countRegister
    }
    return render(Request, 'App/Dashboard.html',context)


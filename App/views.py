# from django.shortcuts import render
# from django.http import HttpRequest,HttpResponse
# from django.shortcuts import render
# # Create your views here.


# def Home(Request):
#     return render(Request ,'App/index.html')

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


from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
# from .models import members
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import  Patient,TuberculosisTests,PneumoniaTests
from django.contrib.auth.models import User
from datetime import datetime
import os
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from Accounts.models import Hospital





def all(Request):
    all = Patient.objects.all().values()
    
    TB = 'TUBERCULOSIS'
    TB_region =TuberculosisTests.objects.raw( "SELECT ID ,COUNT(patientID)count, region  FROM App_TuberculosisTests WHERE pridected = %s GROUP BY region",[TB])
  
   
    for TB_region in TB_region:
        print(TB_region.region)
        
    context={
        "TB_region":TB_region,
        "all":all
    }
    return render(Request,'App/all.html',context)






def TBPridicted():
    TBPridicted =  Patient.objects.filter(pridected = 'TUBERCULOSIS').values
    # Patient.objects.raw( "SELECT ID ,SUM()")
    
    return TBPridicted


def notPridicted(Request):
    username = Request.user.username
    user = User.objects.get(username = username)
    notPridicted =  Patient.objects.filter(isPridicted = False,userName=user).values()
    
    return notPridicted
@login_required(login_url='/login')
def  Home(Request):
    username = Request.user.username
    user = User.objects.get(username = username)
    userNameID =  user
    output = ''
    global pat 
    id = ''
    global imag
    global imagPath
    
    if(Request.method == "POST"):
      
        if Request.POST.get('ID'):
            
           #geting patient
            username = Request.user.username
            
            pat = Patient.objects.filter(patientID =  Request.POST.get("ID"),userName=User.objects.get(username = username)).values()
            if(len(pat) == 0):
                 person = "ma ahan mid jiro shiqsigaan"
                 context= {
                     "person": person,
                     "notPridicted": notPridicted(Request)
                 }
                 return render(Request,"App/index.html",context)
            imag = '/media/'+pat[0]['patientXrayImage']
            imagPath = './media/'+pat[0]['patientXrayImage']
            id = pat[0]['patientID']
        
        
        elif(Request.POST.get('pridicts')):
            isPridictedUpdate = Patient.objects.get(patientID=pat[0]['patientID'])
            isPridictedUpdate.isPridicted = True
            isPridictedUpdate.save()
            path=imagPath
            path=str(path)
            
            
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
                    if ( TuberculosisTests.objects.filter(patientID = id , userName =  userNameID).values()):
                        print("patient exist")
        
                 
                    
                    else:
                        TB = TuberculosisTests(
                                userName = userNameID ,
                                patientID = pat[0]['patientID'] ,
                                patientName = pat[0]['patientName'] ,
                                patientTell =pat[0]['patientTell'] ,
                                paientAge = pat[0]['paientAge'] ,
                                pridected = 'Normal' ,
                                region = pat[0]['region'],
                                patientGenter = pat[0]['patientGenter'] ,
                                patientAddress = pat[0]['patientAddress'] ,
                                patientRegDate = pat[0]['patientRegDate'] ,
                                patientXrayImage = pat[0]['patientXrayImage'] ,
                        )
                        TB.save()
                else:
                   
                    output = "Affected By Tubarculosis"
                    print("Affected By Tubarculosis")
                    username = Request.user.username
                    user = User.objects.get(username = username)
                    userNameID =  user
                    id =   pat[0]['patientID']
                    if ( TuberculosisTests.objects.filter(patientID = id , userName= userNameID).values()):
                        print("patient exist")
        
                    else:
                        TB = TuberculosisTests(
                                userName =  userNameID,
                                patientID = pat[0]['patientID'] ,
                                patientName = pat[0]['patientName'] ,
                                patientTell =pat[0]['patientTell'] ,
                                paientAge = pat[0]['paientAge'] ,
                                region = pat[0]['region'],
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
                    if ( PneumoniaTests.objects.filter(patientID = id , userName =  userNameID).values()):
                        print("patient exist")
                 
                  
                    else:
                        PN = PneumoniaTests(
                                    userName =  userNameID ,
                                    patientID = pat[0]['patientID'] ,
                                    patientName = pat[0]['patientName'] ,
                                    patientTell =pat[0]['patientTell'] ,
                                    region = pat[0]['region'],
                                    paientAge = pat[0]['paientAge'] ,
                                    pridected = 'Normal' ,
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
                    if ( PneumoniaTests.objects.filter(patientID = id , userName =  userNameID).values()):
                        print("patient exist")
                 
                    
                    else :
                            PN = PneumoniaTests(
                                    userName =  userNameID ,
                                    patientID = pat[0]['patientID'] ,
                                    patientName = pat[0]['patientName'] ,
                                    patientTell =pat[0]['patientTell'] ,
                                    paientAge = pat[0]['paientAge'] ,
                                    pridected = 'PNEUMONIA' ,
                                    region = pat[0]['region'],
                                    patientGenter = pat[0]['patientGenter'] ,
                                    patientAddress = pat[0]['patientAddress'] ,
                                    patientRegDate = pat[0]['patientRegDate'] ,
                                    patientXrayImage = 'TB/Tuberculosis/'+pat[0]['patientXrayImage'] 
                            )
                            PN.save()
        else:
             return render(Request,"App/index.html")
        username = Request.user.username
        user = User.objects.get(username = username)
        userNameID =  user
        HospitalInfo = Hospital.objects.filter(userName = userNameID ).values()
        date = datetime.today().strftime('%Y-%m-%d')
       
        
        
        context = {
            "date":date,
            "patient" : pat,
            "imag" : imag,
            "output": output,
            "id": id,
            "HospitalInfo":HospitalInfo,
        
        }
        
        return render(Request,"App/index.html",context)
    
       
        
    else:
      
        context = {
          
            "notPridicted": notPridicted(Request)
        }
     
        return render(Request,"App/index.html",context)

#patient Regestration
@login_required(login_url='/login')
def X_Rey(Request):
    username = Request.user.username
    if Request.method == 'POST':
        
        if (Patient.objects.filter(userName = User.objects.get(username = username) ,patientID = Request.POST.get('id'))):
            found = "this ID " +Request.POST.get('id')+ " is Already exist"
            context = {"found":found}
            return render(Request ,'App/patient.html',context)
            
        else:
            
            name = Request.POST.get('name')
            id = Request.POST.get('id')
            tell = Request.POST.get('tell')
            age = Request.POST.get('age')
            gender = Request.POST.get('gender')
            address = Request.POST.get('address')
            test = Request.POST.get('type')
            Region = Request.POST.get('Region')
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
                    region = Region,
                    patientXrayImage = xrayImage,
                    userName = User.objects.get(username = username)
            )
            pat.save()
    return render(Request ,'App/patient.html')



def allPatients(Request):
    
    if Request.method == 'POST':
        if Request.POST.get('allPatients') == "TB":
            
            username = Request.user.username
            user = User.objects.get(username = username)
            id =  user
            TBPatients = TuberculosisTests.objects.filter(userName = id,  pridected = "TUBERCULOSIS").values()
            context = {
                "TBPatients": TBPatients,
               
            }
            return context
        elif Request.POST.get('allPatients') == "NORMAL":
            
            username = Request.user.username
            user = User.objects.get(username = username)
            id =  user
            TBPatients = TuberculosisTests.objects.filter(userName = id,  pridected = "Normal").values()
            PNPatients = PneumoniaTests.objects.filter(userName = id ,pridected = "Normal").values()
            context = {
                "TBPatients": TBPatients,
                "PNPatients" : PNPatients
               
            }
            return context
        elif Request.POST.get('allPatients') == "PN":
            
            username = Request.user.username
            user = User.objects.get(username = username)
            id =  user
            PNPatients = PneumoniaTests.objects.filter(userName = id ,pridected = "PNEUMONIA").values()
            context = {
                "PNPatients" : PNPatients
               
            }
            return context
        else:
            username = Request.user.username
            user = User.objects.get(username = username)
            usernameID =  user
            TBPatients = TuberculosisTests.objects.filter(userName = usernameID).values()
            PNPatients = PneumoniaTests.objects.filter(userName = usernameID).values()
        


            context = {
                "TBPatients": TBPatients,
                "PNPatients" : PNPatients
            }
            return context
        
           

    else:
        username = Request.user.username
        user = User.objects.get(username = username)
        id =  user
        TBPatients = TuberculosisTests.objects.filter(userName = id).values()
        PNPatients = PneumoniaTests.objects.filter(userName = id).values()
        


        context = {
            "TBPatients": TBPatients,
            "PNPatients" : PNPatients
        }
        return context



def dashboard (Request):
    
    if (Request.user.username):
       
        #TB chart
        TBresults = []
        countTBresults = []
        username = Request.user.username
        user = User.objects.get(username = username)
        id =  user
       
      
        #TB_and_Normal_group_by 
        TB_and_Normal_group_by = TuberculosisTests.objects.values('pridected', ).filter(userName=id).annotate(total=Count('patientID'),).order_by ('pridected') 
        for TB_and_Normal_group_by in TB_and_Normal_group_by:
           
            TBresults.append(TB_and_Normal_group_by['pridected'])
            countTBresults.append(TB_and_Normal_group_by['total'])
        
   
   
        #   PN_and_Normal_group_by 
        PNresults = []
        countPNresults = []
        PN_and_Normal_group_by = PneumoniaTests.objects.values('pridected', ).filter(userName=id,).annotate(total=Count('patientID'),).order_by ('pridected') 
        for PN_and_Normal_group_by in PN_and_Normal_group_by:
           
            PNresults.append(PN_and_Normal_group_by['pridected'])
            countPNresults.append(PN_and_Normal_group_by['total'])
     
      
        
        
        #Main chart
        RegisterYear_monthCount = []
        countRegister = []  
        for results in Patient.objects.raw( "SELECT ID ,COUNT(patientID)count,strftime('%Y-%m', patientRegDate) year_month FROM App_Patient GROUP BY year_month  "):
        
            if (results.userName == id):
                countRegister.append(results.count)
                RegisterYear_monthCount.append(results.year_month)
        
        countTB = len(TuberculosisTests.objects.filter(userName = id,pridected = 'TUBERCULOSIS').values())
        countNormalLtb = len(TuberculosisTests.objects.filter(userName = id,pridected = 'Normal').values())
        countPN = len(PneumoniaTests.objects.filter(userName = id,pridected = 'PNEUMONIA').values())
        countNormalPN = len(PneumoniaTests.objects.filter(userName = id,pridected = 'Normal').values())
        #TB regions
        
        
        
        # Region
        queryset = (TuberculosisTests.objects
            .values(
            'region',
            )
            .filter(
            userName=id,
            )
            .annotate(
            total=Count('region'),
            )
            )
       
        gobolo = {}

        for region in queryset:
          
           gobolo.update({region['region']:region['total']})

        
        
        context = {
            
            "allPatients":allPatients(Request),
            
            "countTB": countTB,
            "countNormalLtb":countNormalLtb,
            "countNormalPN":countNormalPN,
            "countPN": countPN,
            
            
            'PNresults':PNresults,
            'countPNresults':countPNresults,
            'TBresults':TBresults,
            
            'countTBresults':countTBresults,
            'RegisterYear_monthCount':RegisterYear_monthCount,
            'countRegister':countRegister,
            
            "gobolo": gobolo,
            "queryset": queryset,
      
        }
        return render(Request, 'App/Dashboard.html',context)
    else:
         return render(Request, 'App/Dashboard.html')

@login_required(login_url='/login')
def updatePatients(Request,id):
    username = Request.user.username
    user = User.objects.get(username = username)
    update = Patient.objects.get(patientID = id, userName = user) 
    if Request.method == 'POST':
        
            
        name = Request.POST.get('name')
        updateID = Request.POST.get('id')
        
        if (Patient.objects.filter(patientID = updateID, userName = user,isPridicted= False)):
            message = "this" + updateID +" id already exist "
            context = {
            "message":message,
            "upadate":update
            }
            return render(Request,"App/updatePatients.html",context)

        tell = Request.POST.get('tell')
        age = Request.POST.get('age')
        gender = Request.POST.get('gender')
        address = Request.POST.get('address')
        test = Request.POST.get('type')
        Region = Request.POST.get('Region')
    
        username = Request.user.username
        
        
        
        if (len(Request.FILES) != 0):
            if len(update.patientXrayImage)>0:
                os.remove(update.patientXrayImage.path)
            update.patientXrayImage = Request.FILES['xrayImage']
    
        update.patientID = updateID
        update.patientName = name
        update.patientTell = tell
        update.paientAge = age
        update.testType = test
        update.patientGenter = gender
        update.patientAddress = address
        update.region = Region
        update.isPridicted = False
    
        update.save()
        
        
        if ("TB" in id):
            TuberculosisTests.objects.get(patientID = id, userName = user).delete()
        
        if("PN" in id):
            PneumoniaTests.objects.get(patientID = id, userName = user).delete()
        return redirect('/')
   

    else:
        context = {
            "upadate":update
        }
        return render(Request,"App/updatePatients.html",context)
                                   
@login_required(login_url='/login')
def updatePatients2(Request, id):
     
     
    username = Request.user.username
    user = User.objects.get(username = username)
    update = Patient.objects.get(patientID = id, userName = user) 
    if Request.method == 'POST':
        name = Request.POST.get('name')
        id = Request.POST.get('id')
        tell = Request.POST.get('tell')
        age = Request.POST.get('age')
        gender = Request.POST.get('gender')
        address = Request.POST.get('address')
        test = Request.POST.get('type')
        Region = Request.POST.get('Region')
       
        username = Request.user.username
        
        
        
        if (len(Request.FILES) != 0):
            if len(update.patientXrayImage)>0:
                os.remove(update.patientXrayImage.path)
            update.patientXrayImage = Request.FILES['xrayImage']
    
        update.patientID = id
        update.patientName = name
        update.patientTell = tell
        update.paientAge = age
        update.testType = test
        update.patientGenter = gender
        update.patientAddress = address
        update.region = Region
        update.isPridicted = False
       
        update.save()
        
        
  
        return redirect('/predict')
   

    else:
        context = {
            "upadate":update
        }
        return render(Request,"App/updatePatients.html",context)

@login_required(login_url='/login')
def deletePatients(Request, id):
        
    username = Request.user.username
    user = User.objects.get(username = username)
    Patient.objects.get(patientID = id, userName = user).delete()

    return redirect('/predict')


@login_required(login_url='/login')
def deletePatientsDahboard(Request, id):
    username = Request.user.username
    user = User.objects.get(username = username)
    if ("TB" in id):
          TuberculosisTests.objects.get(patientID = id, userName = user).delete()
          Patient.objects.get(patientID = id, userName = user).delete()
         
    if("PN" in id):
             PneumoniaTests.objects.get(patientID = id, userName = user).delete()
             Patient.objects.get(patientID = id, userName = user).delete()
 

    return redirect('/')


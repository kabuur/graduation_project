# from django.shortcuts import render
# from django.http import HttpRequest,HttpResponse
# from django.shortcuts import render
# # Create your views here.


# def Home(Request):
#     return render(Request ,'App/index.html')



from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# from .models import members
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import Patient




import warnings
from PIL import Image, ImageEnhance
warnings.filterwarnings('ignore')
import tensorflow as tf
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np
#from keras.preprocessing import image
import keras.utils as image



def ImageProcessing(Request):
    output = ''
   
    if Request.method == 'POST':
        diseaseType = Request.POST['dis']
        
        # print(diseaseType)
        #save image to the Images folder
        img_file = Request.FILES['name']
        fs = FileSystemStorage()
        
        filename = fs.save('./images/'+img_file.name, img_file)
        print(filename)
        uploaded_file_path = fs.path(filename)
        # print('absolute file path', uploaded_file_path) 
        
        imageRes = Request.FILES['name']
      
      
      
      
        #loading model 
        path=uploaded_file_path
        path=str(path)
        print(path)
        if diseaseType == 'Tubarculosis':
            model=load_model('./TB8-1.h5')
        else:
            model=load_model('./model2.h5')
        
        img_file=image.load_img(path,target_size=(224,224))
        x=image.img_to_array(img_file)
        x=np.expand_dims(x, axis=0)
        img_data=preprocess_input(x)
        classes=model.predict(img_data)
        global result
        result=classes
       



        print(result[0][0])
        
        if diseaseType == 'Tubarculosis':
            if result[0][0]>0.5:
                output = "Result is Normal"
                print("Result is Normal")
                
            else:
                output = "Affected By Tubarculosis"
                print("Affected By Tubarculosis")
        else:
            if result[0][0]>0.5:
                output = "Result is Normal"
                print("Result is Normal")
                
            else:
                output = "Affected By PNEUMONIA"
                print("Affected By PNEUMONIA")


   
   
    context = {
        
        "output" :output,
        
    }
    return context
def  Home(Request):
    diseaseType = 'Tubarculosis'
    output = ''
    global pat 
    id = ''
    global imag
    if(Request.method == "POST"):
        print("the fruist post")
        if Request.POST.get('ID'):
           
            pat = Patient.objects.filter(patientID =  Request.POST.get("ID")).values()
            
            imag = './media/'+pat[0]['patientXrayImage']
            id = pat[0]['patientID']
        
        if(Request.POST.get('ck')):
            print("name is not difined")
            path=imag
            path=str(path)
            print(path)
            if diseaseType == 'Tubarculosis':
                model=load_model('./TB8-1.h5')
            else:
                model=load_model('./model2.h5')
            
            img_file=image.load_img(path,target_size=(224,224))
            x=image.img_to_array(img_file)
            x=np.expand_dims(x, axis=0)
            img_data=preprocess_input(x)
            classes=model.predict(img_data)
            global result
            result=classes
            
            print(result[0][0])
            
            if diseaseType == 'Tubarculosis':
                if result[0][0]>0.5:
                    output = "Result is Normal"
                    print("Result is Normal")
                    
                else:
                    output = "Affected By Tubarculosis"
                    print("Affected By Tubarculosis")
            else:
                if result[0][0]>0.5:
                    output = "Result is Normal"
                    print("Result is Normal")
                    
                else:
                    output = "Affected By PNEUMONIA"
                    print("Affected By PNEUMONIA")
            

        
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
        xrayImage = Request.FILES['xrayImage']
        
        
        
        
        
        # img_file = Request.FILES['X_ray']
        # fs = FileSystemStorage()
        # filename = fs.save('./xray/'+img_file.name, img_file)
        # print(filename)
    return render(Request ,'App/patient.html')




   

   

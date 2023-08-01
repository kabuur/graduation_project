from django.shortcuts import render

from django.http import HttpResponse



from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from Accounts .models import Hospital
from App.models import Patient,TuberculosisTests,PneumoniaTests

# Create your views here.
# Create your views here.





#form of personal user checking


def pateintUser(Requiest):
    
    hospitals = Hospital.objects.all().values()
  


    if Requiest.method == "POST":
        ID = Requiest.POST.get("pateintID")
        TELL = Requiest.POST.get("TELL")
        HOSPITAL = Requiest.POST.get("HOSPITAL")
        HospitaliID = Hospital.objects.get( HospitalName= HOSPITAL)
        id = HospitaliID.userName
        
        
        
        if TuberculosisTests.objects.filter(userName = id,patientID= ID,patientTell = TELL).values():
            patient =  TuberculosisTests.objects.filter(userName = id,patientID= ID,patientTell = TELL).values()
            patientImage =   Patient.objects.filter(userName = id,patientID= ID,patientTell = TELL).values()
            patientImage = "/media/"+patientImage[0]['patientXrayImage']
            test_type = "TUBERCULOSIS"
            
            context = {
                "test_type":test_type,
                'patient': patient,
                "patientImage":patientImage
            }
            return render(Requiest,'PersonalUser/pateintUser.html',context)
        
        
        
        elif PneumoniaTests.objects.filter(userName = id,patientID= ID,patientTell = TELL).values():
            patient =  PneumoniaTests.objects.filter(userName = id,patientID= ID,patientTell = TELL).values()
            patientImage =   Patient.objects.filter(userName = id,patientID= ID,patientTell = TELL).values()
            patientImage = "/media/"+patientImage[0]['patientXrayImage']
            test_type = "PNEUMONIA"
            context = {
                "test_type":test_type,
                'patient': patient,
                "patientImage":patientImage
            }
            return render(Requiest,'PersonalUser/pateintUser.html',context)
        
        
        
        
        else:
            context = {
                "hospitals":hospitals,
                'message': "Ma ahan mid jiro shaqsigaan sorry ......"
            }
            return render(Requiest,'PersonalUser/pateintUser.html',context)
        
        
    
    
    
    
 
    
    context = {
        "hospitals":hospitals
    }
    
    return render(Requiest,'PersonalUser/pateintUser.html',context)

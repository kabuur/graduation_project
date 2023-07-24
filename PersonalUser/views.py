from django.shortcuts import render

from django.http import HttpResponse



from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from Accounts .models import Hospital
from App.models import Patient

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
        if(Patient.objects.filter(userName = id,patientID= ID,isPridicted = True,patientTell = TELL).values()):
            patient =  Patient.objects.filter(userName = id,patientID= ID,isPridicted = True,patientTell = TELL).values()
            context = {
                'patient': patient
            }
            return render(Requiest,'PersonalUser/pateintUser.html',context)
            
        
        # id = User.objects.get(username = )
        # if(Patient.objects.filter(patientID = ID, patientTell = TELL,)):
    
    
    
    
 
    
    context = {
        "hospitals":hospitals
    }
    
    return render(Requiest,'PersonalUser/pateintUser.html',context)

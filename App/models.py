from django.db import models
from django.contrib.auth.models import User
from Accounts.models import  Hospital
# Create your models here.


    
    
class Patient(models.Model):
    
    userName = models.ForeignKey(User, null = False, on_delete = models.CASCADE)
    patientID = models.CharField(max_length=50)
    patientName = models.CharField(max_length=100)
    patientTell = models.CharField(max_length= 100)
    paientAge = models.IntegerField()
    region = models.CharField(max_length=900)
    testType = models.CharField(max_length=100)
    patientGenter = models.CharField(max_length=100)
    patientAddress = models.CharField(max_length=100)
    patientRegDate = models.DateTimeField(auto_now_add=True)
    isPridicted = models.BooleanField(default=False)
    patientXrayImage = models.ImageField(upload_to = 'xray')
    
    def __str__(self):
        return self.patientName


class TuberculosisTests(models.Model):
    
    userName =  models.IntegerField()
    patientID = models.CharField(max_length=50)
    patientName = models.CharField(max_length=100)
    patientTell = models.CharField(max_length= 100)
    paientAge = models.IntegerField()
    region = models.CharField(max_length=900)
    pridected = models.CharField(max_length=100)
    patientGenter = models.CharField(max_length=100)
    patientAddress = models.CharField(max_length=100)
    patientRegDate = models.DateField(auto_now_add=True)
    patientXrayImage = models.ImageField(upload_to = 'TB/Tuberculosis')
    def __str__(self):
        return self.patientName
    



    
    
    

class PneumoniaTests(models.Model):
    userName =  models.IntegerField()
    patientID = models.CharField(max_length=50)
    patientName = models.CharField(max_length=100)
    patientTell = models.CharField(max_length= 100)
    paientAge = models.IntegerField()
    region = models.CharField(max_length=900)
    pridected = models.CharField(max_length=100)
    patientGenter = models.CharField(max_length=100)
    patientAddress = models.CharField(max_length=100)
    patientRegDate = models.DateTimeField(auto_now_add=True)
    patientXrayImage = models.ImageField(upload_to = 'PN/Pneumonia')
    def __str__(self):
        return self.patientName   
    

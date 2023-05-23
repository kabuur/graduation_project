from django.db import models
from django.contrib.auth.models import User
from Accounts.models import  Hospital
# Create your models here.


    
    
class Patient(models.Model):
    
    userName = models.ForeignKey(User, null = False, on_delete = models.CASCADE)
    patientID = models.CharField(max_length=50,unique=True)
    patientName = models.CharField(max_length=100)
    patientTell = models.CharField(max_length= 100)
    paientAge = models.IntegerField()
    testType = models.CharField(max_length=100)
    patientGenter = models.CharField(max_length=100)
    patientAddress = models.CharField(max_length=100)
    patientRegDate = models.DateTimeField(auto_now_add=True)
    patientXrayImage = models.ImageField(upload_to = 'xray')
    
    def __str__(self):
        return self.patientName


class Tuberculosis(models.Model):
    
    userName =  models.IntegerField()
    patientID = models.CharField(max_length=50,unique=True)
    patientName = models.CharField(max_length=100)
    patientTell = models.CharField(max_length= 100)
    paientAge = models.IntegerField()
    pridected = models.CharField(max_length=100)
    patientGenter = models.CharField(max_length=100)
    patientAddress = models.CharField(max_length=100)
    patientRegDate = models.DateTimeField(auto_now_add=True)
    patientXrayImage = models.ImageField(upload_to = 'TB/Tuberculosis')
    def __str__(self):
        return self.patientName
    

class NormalTB(models.Model):
    
    userName =  models.IntegerField()
    patientID = models.CharField(max_length=50,unique=True)
    patientName = models.CharField(max_length=100)
    patientTell = models.CharField(max_length= 100)
    paientAge = models.IntegerField()
    pridected = models.CharField(max_length=100)
    patientGenter = models.CharField(max_length=100)
    patientAddress = models.CharField(max_length=100)
    patientRegDate = models.DateTimeField(auto_now_add=True)
    patientXrayImage = models.ImageField(upload_to = 'TB/Normal')
    def __str__(self):
        return self.patientName
    
    
    

class Pneumonia(models.Model):
    
    userName =  models.IntegerField()
    patientID = models.CharField(max_length=50,unique=True)
    patientName = models.CharField(max_length=100)
    patientTell = models.CharField(max_length= 100)
    paientAge = models.IntegerField()
    pridected = models.CharField(max_length=100)
    patientGenter = models.CharField(max_length=100)
    patientAddress = models.CharField(max_length=100)
    patientRegDate = models.DateTimeField(auto_now_add=True)
    patientXrayImage = models.ImageField(upload_to = 'PN/Pneumonia')
    def __str__(self):
        return self.patientName   
    
class NormalPN(models.Model):
    
    userName =  models.IntegerField()
    patientID = models.CharField(max_length=50, unique=True)
    patientName = models.CharField(max_length=100)
    patientTell = models.CharField(max_length= 100)
    paientAge = models.IntegerField()
    pridected = models.CharField(max_length=100)
    patientGenter = models.CharField(max_length=100)
    patientAddress = models.CharField(max_length=100)
    patientRegDate = models.DateTimeField(auto_now_add=True)
    patientXrayImage = models.ImageField(upload_to = 'PN/Pneumonia')
    def __str__(self):
        return self.patientName
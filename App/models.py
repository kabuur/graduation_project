from django.db import models
# Create your models here.

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    userName = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    emal = models.CharField(max_length=100)
    tell = models.CharField(max_length=100)
    registerDate = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    
class Patient(models.Model):
    patientID = models.CharField(max_length=50)
    patientName = models.CharField(max_length=100)
    patientTell = models.CharField(max_length= 100)
    paientAge = models.IntegerField()
    patientGenter = models.CharField(max_length=100)
    patientAddress = models.CharField(max_length=100)
    patientRegDate = models.DateTimeField(auto_now_add=True)
    patientXrayImage = models.ImageField(upload_to = 'xray')
    
    def __str__(self):
        return self.patientName


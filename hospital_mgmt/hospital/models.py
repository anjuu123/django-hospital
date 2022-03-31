from datetime import date
from time import time
from unicodedata import name
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    speciality = models.CharField(max_length=50)



class Patient(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(null=True)
    address = models.TextField()


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

class Summary(models.Model):
    
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=50, blank=True, null=True)
    detail = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle

    def get_absolute_url(self):
    	return reverse('summary-list')

class TypeOfStudy(models.Model):
    
    
    s_no = models.CharField(max_length=1000)
    type_of_study = models.CharField(max_length=500)
    stemmed = ArrayField(models.CharField(max_length=360), blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type_of_study

class DeviceType(models.Model):
    
    
    s_no = models.CharField(max_length=1000)
    device_type = models.CharField(max_length=360)
    device_maker = models.CharField(max_length=360)
    device_type_stemmed = ArrayField(models.CharField(max_length=360), blank=True)
    device_maker_stemmed = ArrayField(models.CharField(max_length=360), blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device_type

class DiseaseType(models.Model):
    
    
    s_no = models.CharField(max_length=1000)
    disease_type = models.CharField(max_length=50)
    stemmed = ArrayField(models.CharField(max_length=360), blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.disease_type

class PatientGroup(models.Model):
    
    
    s_no = models.CharField(max_length=1000)
    patient_group = models.CharField(max_length=50)
    stemmed = ArrayField(models.CharField(max_length=360), blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient_group

class ProcedureType(models.Model):
    
    
    s_no = models.CharField(max_length=1000)
    procedure_type = models.CharField(max_length=50)
    stemmed = ArrayField(models.CharField(max_length=360), blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.procedure_type




    




    
 


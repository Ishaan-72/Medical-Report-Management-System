from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Report(models.Model):
    patientname=models.CharField(max_length=122)
    doctorname=models.CharField(max_length=122)
    reportdate=models.DateField()
    image= models.ImageField(upload_to="reportsdir",default="") 
    user=models.ForeignKey(User, on_delete=models.CASCADE)
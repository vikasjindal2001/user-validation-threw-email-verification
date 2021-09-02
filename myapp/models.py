from django.db import models

# Create your models here.
class registrations(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    phonenumber=models.CharField(max_length=10)
    countrycode=models.CharField(max_length=4)
    password=models.CharField(max_length=30)
    email=models.CharField(max_length=45)
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
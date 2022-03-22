from django.db import models

# Create your models here.
class Users(models.Model):

    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=8)
    email=models.CharField(max_length=20)
    phone=models.IntegerField()
    


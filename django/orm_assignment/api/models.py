from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.EmailField(default="xyz@gmail.com")
    floor=models.IntegerField()
    resources=models.CharField(max_length=25)


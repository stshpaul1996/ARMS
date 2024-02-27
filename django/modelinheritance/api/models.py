from django.db import models

# Create your models here.


class City(models.Model):
    pincode=models.IntegerField(max_length=25)
    city=models.CharField(max_length=25)

class Student(City):
    name=models.CharField(max_length=25)
    address=models.CharField(max_length=25)
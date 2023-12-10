from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=200)
    address = models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    cust_id=models.SmallIntegerField(default=0)
    aadhar=models.BigIntegerField(default=0)
    value_less_zero=NegativeIntegerField(default=-1)
    min_value_id=models.SmallIntegerField(default=23,validators=[MinValueValidator(limit_value=23,message="value should greater than zero")])
    



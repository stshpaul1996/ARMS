from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

# def validate_name(value):
#     if not value.isupper():
#         raise ValidationError('Enter valid name')

class Student(models.Model):
    name=models.CharField(max_length=50,unique=True )
    email=models.EmailField(max_length=50,default='')
    age=models.IntegerField(default=0)

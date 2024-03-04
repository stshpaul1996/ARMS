from typing import Collection
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def emailValidate(email):
    if not email.endswith(".com"):
        raise ValidationError("email does not ends with .com")
    return email
class Details(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(validators = [emailValidate])
    floor = models.IntegerField()
    resources = models.CharField(max_length=50)
    
        
        

    
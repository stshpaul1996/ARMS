from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def check_spcial_symbols(value):
    if not value.isalnum():
        raise ValidationError("Expecting alpha numeric value")

class Cricketers(models.Model):
    name = models.CharField(max_length=250, validators=(check_spcial_symbols,))
    image_path = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)

# class Person(models.Model):
#     name = models.CharField(max_length=250)
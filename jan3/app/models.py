from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


# def email_validate(value):
#     if not value.isdigit():
#         raise ValidationError("alphabets only")

class Person(models.Model):
    name=models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=100)
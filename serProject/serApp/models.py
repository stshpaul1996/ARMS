from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

from django.db import models

# def check_number(value):
#     if len(value)<7:
#         raise ValidationError("enter 7 characters ")
    
class Student(models.Model):
    name=models.CharField(max_length=50,unique=True)
    rollno=models.IntegerField()
    age=models.IntegerField()

    def clean_age(self):
        if self.age <0:
            raise ValidationError("Enter valid age")
        return self.age
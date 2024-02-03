from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
class MyUser(AbstractUser):
    Aadhar_number=models.IntegerField(default=0)
    def clean(self):
        super().clean()
        if len(str(self.Aadhar_number)) != 12:
            raise ValidationError("Aadhar number must be 12 digits long.")
    def __str__(self):
        return self.first_name



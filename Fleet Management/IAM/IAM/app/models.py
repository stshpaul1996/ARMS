from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)

class MyUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.PROTECT,default=1)
    Aadhar_number=models.IntegerField(default=0)
    def clean(self):
        super().clean()
        if len(str(self.Aadhar_number)) != 12:
            raise ValidationError("Aadhar number must be 12 digits long.")
    def __str__(self):
        return self.first_name

class Api(models.Model):
    name=models.CharField(max_length=200)

class Permissions(models.Model):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    api = models.ForeignKey(Api, on_delete=models.PROTECT)
    has_get = models.BooleanField(default=False)
    has_post = models.BooleanField(default=False)
    has_put = models.BooleanField(default=False)
    has_delete = models.BooleanField(default=False)
    has_patch = models.BooleanField(default=False)




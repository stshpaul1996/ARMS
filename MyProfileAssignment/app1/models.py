from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Api(models.Model):
    name = models.CharField(max_length=250, unique=True)

class Permissions(models.Model):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    api = models.ForeignKey(Api, on_delete=models.PROTECT)
    has_get = models.BooleanField(default=False)
    has_post = models.BooleanField(default=False)
    has_put = models.BooleanField(default=False)
    has_delete = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)



        



    


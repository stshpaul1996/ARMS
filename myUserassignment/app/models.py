from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class BaseAbsrtract(models.Model):
    name = models.CharField(max_length = 100)

    class Meta:
        abstract = True 

class Role(BaseAbsrtract):
    pass 

class API(BaseAbsrtract):
    pass 

class MyUser(AbstractUser):
    role = models.ForeignKey(Role,on_delete = models.PROTECT)

class Permissions(models.Model):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    api = models.ForeignKey(API, on_delete=models.PROTECT)
    has_get = models.BooleanField(default=False)
    has_post = models.BooleanField(default=False)
    has_put = models.BooleanField(default=False)
    has_delete = models.BooleanField(default=False)

class Person(BaseAbsrtract):
    #name = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250, default="")
    age = models.IntegerField(default=0)
    created_by = models.ForeignKey(MyUser, on_delete=models.PROTECT, null=True)
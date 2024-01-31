from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser


# create MyUser model, this has to overide the existing user table. 
#add role column to it.
#develop /role and /user APIs

class BaseAbstarctModel(models.Model):
     name = models.CharField(max_length=250, unique=True)
     class Meta:
         abstract = True

class Role(BaseAbstarctModel):
    pass
    #name = models.CharField(max_length=100, unique=True)

class Api(BaseAbstarctModel):
    pass
    #name = models.CharField(max_length=250, unique=True)

class MyUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.PROTECT, default=1)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
     

class Permissions(models.Model):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    api = models.ForeignKey(Api, on_delete=models.PROTECT)
    has_get = models.BooleanField(default=False)
    has_post = models.BooleanField(default=False)
    has_put = models.BooleanField(default=False)
    has_delete = models.BooleanField(default=False)



        



    


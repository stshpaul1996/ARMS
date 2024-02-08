from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser,Group
from django.contrib.auth.models import Permission



class BaseAbstractionModel(models.Model):
    name = models.CharField(max_length=250,unique=True)
    class Meta:
        abstract=True


class Role(BaseAbstractionModel):
    pass

class MyUser(AbstractUser):
    role=models.ForeignKey(Role, on_delete=models.PROTECT,null=True)
  
    

class Api(BaseAbstractionModel):
    pass
    #name = models.CharField(max_length=250, unique=True)



class Permissions(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.PROTECT,null=True)
    role_id = models.ForeignKey(Role, on_delete=models.PROTECT)
    api_id = models.ForeignKey(Api, on_delete=models.PROTECT)
    has_get = models.BooleanField(default=False)
    has_post = models.BooleanField(default=False)
    has_put = models.BooleanField(default=False)
    has_delete = models.BooleanField(default=False)

class Person(models.Model):
    name =models.CharField(max_length=250,default="")
    age = models.IntegerField(default=0)
    created_by = models.ForeignKey(MyUser,on_delete=models.PROTECT,null=True)

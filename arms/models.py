from django.db import models
# from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

class BaseAbstarctModel(models.Model):
     name = models.CharField(max_length=250, unique=True)
     class Meta:
        abstract = True

class Role(BaseAbstarctModel):
    pass
    #name = models.CharField(max_length=100, unique=True)

class MyUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.PROTECT,default = 1)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #role_inst = Role.objects.get(id=kwargs.get("role_id"))


class trip(models.Model):
    name = models.CharField(max_length= 250)

class member(models.Model):
    name = models.CharField(max_length=250)
    trip_id = models.ForeignKey(trip,on_delete = models.PROTECT)

class expenses(models.Model):
    total_amount = models.IntegerField()
    reasons = models.CharField(max_length =250)  
    trip_id = models.ForeignKey(trip,on_delete = models.PROTECT)


class Api(BaseAbstarctModel):
    pass
    #name = models.CharField(max_length=250, unique=True)

class Permission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    api = models.ForeignKey(Api, on_delete=models.PROTECT)
    user_id  = models.ForeignKey(MyUser,on_delete = models.PROTECT,default = 1)
    has_get = models.BooleanField(default=False)
    has_post = models.BooleanField(default=False)
    has_put = models.BooleanField(default=False)
    has_delete = models.BooleanField(default=False)



from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class NameAbstractModel(models.Model):
    name=models.CharField(max_length=100,unique=True)
    class Meta:
        abstract = True

class Role(NameAbstractModel):
    pass

class MyUser(AbstractUser):
    role=models.ForeignKey(Role,on_delete=models.PROTECT)

class Department(models.Model):
    dname=models.CharField(max_length=100)
    dlocation=models.CharField(max_length=100)

class Employee(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.PROTECT)
    ename=models.CharField(max_length=100)
    esal=models.IntegerField()
    eaddress=models.CharField(max_length=100)

class Api(models.Model):
    name=models.CharField(max_length=100)

class Permission(models.Model):
    role=models.ForeignKey(Role,on_delete=models.PROTECT)
    api=models.ForeignKey(Api,on_delete=models.PROTECT)
    user=models.ForeignKey(MyUser,on_delete=models.PROTECT)
    has_get=models.BooleanField(default=False)
    has_post=models.BooleanField(default=False)
    has_put=models.BooleanField(default=False)
    has_delete=models.BooleanField(default=False)


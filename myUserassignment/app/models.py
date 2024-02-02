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
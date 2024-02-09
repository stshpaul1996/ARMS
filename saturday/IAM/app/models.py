from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseAbstractionModel(models.Model):
    voter_number=models.CharField(max_length=100,unique=True)
    class Meta:
        abstract=True 

class Person(BaseAbstractionModel):
    pass

class MyUser(AbstractUser):
    number=models.ForeignKey(Person, on_delete=models.PROTECT,null=True)


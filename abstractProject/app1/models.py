from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length = 100,unique = True)

class Api(models.Model):
    name = models.CharField(max_length = 100,unique = True)

class Permissions(models.Model):
    role = models.ForeignKey(Role,on_delete = models.PROTECT)
    api = models.ForeignKey(Api,on_delete = models.PROTECT)
    has_get = models.BooleanField(default = False)
    has_post = models.BooleanField(default = False)
    has_put = models.BooleanField(default = False)
    has_delete = models.BooleanField(default = False)

class UsereProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.PROTECT)
    role = models.ForeignKey(Role,on_delete = models.PROTECT)


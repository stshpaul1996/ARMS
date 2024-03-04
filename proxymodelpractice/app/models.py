from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class UserProfile(User):
    aadhar = models.IntegerField()
    pancard = models.CharField(max_length = 100)

class ParentModel(models.Model):
    common_field = models.CharField(max_length=100)
    age = models.IntegerField()

class ChildModel(ParentModel):
    specific_field = models.CharField(max_length=100)
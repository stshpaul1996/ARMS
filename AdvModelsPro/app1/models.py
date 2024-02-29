from django.db import models
from django.contrib.auth.models import User

'''
1. Whenever inheritance model created it internally takes one to one field
2. So we must pass the parent and child class field names for the inheritanced model

'''

# Create your models here.
class UserProfile(User):
    adhaar = models.IntegerField()
    pancard = models.CharField(max_length=100)


from django.db import models

# Create your models here.
from django.db import models

class Visit(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    floor = models.IntegerField()
    resource = models.CharField(max_length=50)

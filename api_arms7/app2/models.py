from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 25)
    age = models.IntegerField()

class Department(models.Model):
    name = models.CharField(max_length = 25)
    num = models.IntegerField()
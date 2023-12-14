from django.db import models

# Create your models here.
class Cricketers(models.Model):
    name = models.CharField(max_length=250)
    image_path = models.CharField(max_length=250)

class Person(models.Model):
    name = models.CharField(max_length=250)
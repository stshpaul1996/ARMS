from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=500)
    content = models.TextField()
    img = models.CharField(max_length=500)
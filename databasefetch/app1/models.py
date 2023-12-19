from django.db import models

# Create your models here.
class Gun(models.Model):
    name = models.CharField(max_length= 250)
    description = models.TextField()
    image_path = models.CharField(max_length= 250)
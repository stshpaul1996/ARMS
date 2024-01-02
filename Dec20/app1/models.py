from django.db import models

# Create your models here.
class MediaDB(models.Model):
    name= models.CharField(max_length=250)
    image = models.ImageField()
    video = models.FileField()
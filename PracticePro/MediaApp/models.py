from django.db import models

# Create your models here.
class MediaDB(models.Model):
    name= models.CharField(max_length=250)
    image = models.ImageField(upload_to="")
    video = models.FileField(upload_to="")
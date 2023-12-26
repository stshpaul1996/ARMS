from django.db import models

# Create your models here.
class Media(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField()
    age=models.IntegerField()
    video=models.FileField()
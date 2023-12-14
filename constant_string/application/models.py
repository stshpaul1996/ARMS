from django.db import models

# Create your models here.
class display(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    image_path=models.CharField(max_length=250)
    
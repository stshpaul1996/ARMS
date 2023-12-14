from django.db import models

class Tourist_places(models.Model):
    name=models.CharField(max_length=100)
    image=models.CharField(max_length=250)
    content=models.CharField(max_length=300)


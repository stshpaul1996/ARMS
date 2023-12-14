from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=50,null=True,verbose_name='Product Name')
    price=models.FloatField(max_length=20,null=True,verbose_name='price')
    img=models.CharField(max_length=100,null=True,verbose_name='Upload Image')
    
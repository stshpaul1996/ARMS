from django.db import models

def fun(x:int, y:float):
    print(x,y)
fun(1.2,3)

# Create your models here.
class Customer(models.Model):

    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

class Orders(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order_name = models.CharField(max_length=250)
    price = models.IntegerField()
    descrpition = models.TextField()
    location = models.CharField(max_length=250)
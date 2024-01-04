from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validate_email(value):
    if value.isdigit():
        raise ValidationError("expecting alphanueric values")
class Category(models.Model):
    name = models.CharField(max_length=250)    

class SalesOrder(models.Model):
    description = models.TextField(max_length=250)

class PurchaseOrder(models.Model):
    description = models.TextField(max_length=250)
class Product(models.Model):
    name = models.CharField(max_length=250)
    product_unque_number = models.CharField(max_length=250, unique=True)  
    category = models.ForeignKey(Category, on_delete=models.PROTECT) 
    purchase_orders = models.ManyToManyField(PurchaseOrder)
    sales_orders = models.ManyToManyField(SalesOrder)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
class OpeningStock(models.Model):
    prodcut = models.ForeignKey(Product, on_delete=models.PROTECT)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
"""
productpurachaseorder
id
product_id
purchaseorder_id

productsalesoredder
id
product_id
salesorder_id
"""
#stock on hand




class Person(models.Model):
    name = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250, default="", validators=(validate_email,))
    age = models.IntegerField(default=0)

# class Region(models.Model):
#     name = models.CharField(max_length=250, unique=True)

# class Country(models.Model):
#     name = models.CharField(max_length=250, unique=True)
#     region = models.ForeignKey(Region, on_delete=models.PROTECT)

# class State(models.Model):
#     name = models.CharField(max_length=250, unique=True)
#     country = models.ForeignKey(Country, on_delete=models.PROTECT)
# class Address(models.Model):
#     city = models.CharField(max_length=250)
#     street = models.CharField(max_length=250)
#     pincode = models.CharField(max_length=50)


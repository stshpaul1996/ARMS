from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

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

class ProductCost(models.Model):
    prodcut = models.ForeignKey(Product, on_delete=models.PROTECT)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    
class OpeningStock(models.Model):
    prodcut = models.ForeignKey(Product, on_delete=models.PROTECT)
    stock = models.DecimalField(max_digits=10, decimal_places=2)









# Create your models here.

from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250,unique = True)    

class SalesOrder(models.Model):
    description = models.TextField(max_length=250)
    created = models.DateTimeField(default=timezone.now)

class PurchaseOrder(models.Model):
    description = models.TextField(max_length=250)
    created = models.DateTimeField(default=timezone.now)



class Product(models.Model):
    name = models.CharField(max_length=250)
    product_unque_number = models.CharField(max_length=250, unique=True)  
    category = models.ForeignKey(Category, on_delete=models.PROTECT) 
    sales_orders = models.ManyToManyField(SalesOrder, blank=True)
    purchase_orders = models.ManyToManyField(PurchaseOrder, blank=True)

class ProductPurchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    purchase = models.ForeignKey(PurchaseOrder, on_delete=models.PROTECT)
    stock = models.PositiveIntegerField()

class ProductSales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    sales = models.ForeignKey(SalesOrder, on_delete=models.PROTECT)
    stock = models.IntegerField()

# class ProductPurchase(models.Model):
#     product = models.ForeignKey(Product,on_delete = models.PROTECT)
#     purchase = models.ForeignKey(PurchaseOrder,on_delete = models.PROTECT)
#     stock = models.PositiveIntegerField()

# class ProductSales(models.Model):
#     product = models.ForeignKey(Product,on_delete = models.PROTECT)
#     sales = models.ForeignKey(SalesOrder,on_delete = models.PROTECT)
#     stock = models.IntegerField()
    

class ProductCost(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

class OpeningStock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateField(default=timezone.now)

class Stock(models.Model):
    product = models.ForeignKey(Product,on_delete = models.PROTECT)
    description = models.TextField()
    refid = models.IntegerField(default = 0)
    type = models.CharField(max_length=100)
    stock = models.IntegerField()

from django.db import models
from django.core.exceptions import ValidationError
from datetime import timezone,date
# Create your models here.

def validate_date_not_in_future(value):
    if value >date.today():
        raise ValidationError('Date cannot be in the future.')
class Category(models.Model):
    # id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
class PurchaseOrder(models.Model):
    description =models.TextField(max_length=250)
    created=models.DateField(validators=[validate_date_not_in_future])


class SalesOrder(models.Model):
    description = models.TextField(max_length=250)
    created = models.DateField(validators=[validate_date_not_in_future])


class Product(models.Model):
    name = models.CharField(max_length=100)
    categoryid=models.ForeignKey(Category,on_delete=models.PROTECT)
    uniquenumber=models.IntegerField(unique=True)
    purchase_orders = models.ManyToManyField(PurchaseOrder)
    sales_orders = models.ManyToManyField(SalesOrder)

    def __str__(self):
        return self.name
class ProductCost(models.Model):
    productid=models.ForeignKey(Product,on_delete=models.PROTECT)
    cost=models.DecimalField(max_digits=10, decimal_places=2)
    date=models.DateField(validators=[validate_date_not_in_future])

    def __str__(self):
        self.date

class OpeningStock(models.Model):
    productid=models.ForeignKey(Product,on_delete=models.PROTECT)
    stock=models.IntegerField()
    date=models.DateField(validators=[validate_date_not_in_future])

    def __str__(self):
        self.date

class ProductPurchases(models.Model):
    productid=models.ForeignKey(Product,on_delete=models.PROTECT)
    purchaseorderid=models.ForeignKey(PurchaseOrder,on_delete=models.PROTECT)
    stock=models.IntegerField()

    def __str__(self):
        return self.stock
class ProductSales(models.Model):
    productid=models.ForeignKey(Product,on_delete=models.PROTECT)
    salesorderid=models.ForeignKey(SalesOrder,on_delete=models.PROTECT)
    stock=models.IntegerField()


    def __str__(self):
        return self.stock

class Stock(models.Model):
    description=models.CharField(max_length=300)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    refid=models.IntegerField()
    type =models.CharField(max_length=20)
    stock =models.IntegerField()

    def __str__(self):
        return self.stock

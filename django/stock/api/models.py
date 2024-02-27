from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=50)

class Product(models.Model):
    name=models.CharField(max_length=50)
    costprice=models.FloatField(max_length=50)
    salesprice=models.FloatField(max_length=50)

class Purchase(models.Model):
    description=models.CharField(max_length=50)

class Sales(models.Model):
    description=models.CharField(max_length=50)
    customer_id=models.ForeignKey(Customer,on_delete=models.PROTECT)

class Purchaseorder(models.Model):
    purchase=models.ForeignKey(Purchase,on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quatity=models.IntegerField()

class Salesorder(models.Model):
    sales=models.ForeignKey(Sales,on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quatity=models.IntegerField()


    
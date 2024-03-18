from django.db import models
 
class Customer(models.Model):
    name=models.CharField(max_length=100)
 
class Product(models.Model):
    name=models.CharField(max_length=100)
    cost_price=models.IntegerField()
    sales_price=models.IntegerField()
 
class Purchases(models.Model):
    description=models.CharField(max_length=100)
 
class Sales(models.Model):
    description=models.CharField(max_length=100)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
 
class PurchaseOrders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    purchase=models.ForeignKey(Purchases,on_delete=models.CASCADE)
    quantity=models.IntegerField()
 
class SalesOrders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    sales=models.ForeignKey(Sales,on_delete=models.CASCADE)
    quantity=models.IntegerField()
 
 
 
 
 
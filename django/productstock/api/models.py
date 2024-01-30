from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)    

class Product(models.Model):
    name = models.CharField(max_length=250)
    product_unique_number = models.CharField(max_length=250, unique=True)  
    category = models.ForeignKey(Category, on_delete=models.PROTECT) 
     
class OpeningStock(models.Model):
    prodcut = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_stock')
    stock = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    created_date=models.DateTimeField(auto_now_add=True)

class CostPrice(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product_costs')
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_date=models.DateTimeField(auto_now_add=True)

class PPOS(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    description=models.TextField(max_length=250)
    purchasestock  = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    created_date=models.DateTimeField(auto_now_add=True)

class SSOS(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    description=models.TextField(max_length=250)
    salestock = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    created_date=models.DateTimeField(auto_now_add=True)

class Stock(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.TextField(max_length=250,default='super')
    type=models.CharField(max_length=25,default='nill')
    stock=models.DecimalField(max_digits=10,decimal_places=2,default=0,null=True)





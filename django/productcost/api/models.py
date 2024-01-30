
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)    

class SalesOrder(models.Model):
    description = models.TextField(max_length=250,null=True,blank=True)
    

class PurchaseOrder(models.Model):
    description = models.TextField(max_length=250,null=True,blank=True)
    

class Product(models.Model):
    name = models.CharField(max_length=250)
    product_unique_number = models.CharField(max_length=250, unique=True)  
    category = models.ForeignKey(Category, on_delete=models.PROTECT) 
    # purchase_orders = models.ManyToManyField(PurchaseOrder)
    # sales_orders = models.ManyToManyField(SalesOrder)


 
class OpeningStock(models.Model):
    prodcut = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_stock')
    stock = models.DecimalField(max_digits=10, decimal_places=2)

class CostPrice(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product_costs')
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_date=models.DateTimeField(auto_now_add=True)

class PPOS(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    purchase_id = models.ForeignKey(PurchaseOrder,on_delete=models.CASCADE)
    stock  = models.DecimalField(max_digits=10,decimal_places=2)


class SSOS(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    sale_id = models.ForeignKey(SalesOrder,on_delete=models.CASCADE)
    stock = models.DecimalField(max_digits=10,decimal_places=2)

class Stock(models.Model):
    description = models.TextField(max_length=250,default='super')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    type=models.CharField(max_length=25,default='0')
    stock=models.DecimalField(max_digits=10,decimal_places=2,default=0)

class FinalStockReport(models.Model):
    name = models.CharField(max_length=250)
    product_unique_number = models.CharField(max_length=250, unique=True,null=True)  
    category = models.ForeignKey(Category, on_delete=models.PROTECT,null=True)
    product_id=models.ForeignKey(Product,on_delete=models.PROTECT,null=True,related_name='purchase_stock')
    oenping_stock=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    purchasestock=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    salestock=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    totalstock=models.DecimalField(max_digits=10,decimal_places=2,null=True)

"""
productpurachaseorder
id
product_id
purchaseorder_id

productsalesorder
id
product_id
salesorder_id
"""
#stock on hand



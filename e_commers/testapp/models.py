from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

from django.db import models

# Create your models here.





class category(models.Model):
    name = models.CharField(max_length=250)

    

class PurchaseOrder(models.Model):
    description = models.TextField(max_length=250)

class SalesOrder(models.Model):
    description = models.TextField(max_length=250)
class product(models.Model):
    name = models.CharField(max_length=250,unique=True)
    product_unq_number = models.IntegerField()
    category_id = models.ForeignKey(category,on_delete=models.PROTECT)
    purchase_details = models.ManyToManyField(PurchaseOrder,blank=True)
    sales_details = models.ManyToManyField(SalesOrder,blank=True)



class stock(models.Model):
    product_id = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10,decimal_places=2)

class productcost(models.Model):
    product_id = models.ForeignKey(product,on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

class ppos(models.Model):
    product_id = models.ForeignKey(product,on_delete=models.CASCADE)
    purchase_id = models.ForeignKey(PurchaseOrder,on_delete=models.CASCADE)
    quantity  = models.DecimalField(max_digits=10,decimal_places=2)


class ssos(models.Model):
    product_id = models.ForeignKey(product,on_delete=models.CASCADE)
    sale_id = models.ForeignKey(SalesOrder,on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10,decimal_places=2)


class StockReport(models.Model):
    description = description = models.TextField(max_length=250)
    product_id = models.ForeignKey(product,on_delete=models.CASCADE)
    #ref_id = models.IntegerField()
    type = models.CharField(max_length=250)
    quantity = models.DecimalField(max_digits=10,decimal_places=2)

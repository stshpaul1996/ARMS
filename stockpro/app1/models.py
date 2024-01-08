from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)


class Product(models.Model):
    name = models.CharField(max_length=250)
    unique_num = models.CharField(max_length=250, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete= models.PROTECT)
    # sales_orders = models.ManyToManyField(Sales, blank=True)
    # purchase_orders = models.ManyToManyField(Purchase, blank=True)



class OpeningStock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    stock = models.IntegerField()


class ProductCosts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    cost = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

class Sales(models.Model):
    stock = models.IntegerField()
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

class Purchase(models.Model):
    stock = models.IntegerField()
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


# class Stock(models.Model):
#     sales = models.ForeignKey(Sales, on_delete=models.PROTECT)
#     purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT)
    
    

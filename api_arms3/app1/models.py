from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 250)

class Product(models.Model):
    name = models.CharField(max_length=250)
    unique_num = models.CharField(max_length=250, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete= models.PROTECT)

class OpeningStock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    stock = models.IntegerField()

class Sales(models.Model):
    stock = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

class Purchase(models.Model):
    stock = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

class Stock(models.Model):
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    openingStock = models.IntegerField(null = True)
    sales = models.IntegerField(null = True)
    purchase = models.IntegerField(null = True)
    unique_nums = models.CharField(max_length= 250,)


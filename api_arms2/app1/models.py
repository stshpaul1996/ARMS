from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 500, unique = True)

class OpeningStock(models.Model):
    name = models.ForeignKey(Product, on_delete= models.PROTECT)
    units = models.IntegerField()

class Selling(models.Model):
    name = models.ForeignKey(Product, on_delete= models.PROTECT)
    units = models.IntegerField()
    
    def save(self, *args, **kwargs):
        if self.quantity > 0:
            self.quantity *= -1
        super().save(*args, **kwargs)


class Purchasing(models.Model):
    name = models.ForeignKey(Product, on_delete= models.PROTECT)
    units = models.IntegerField()
    
class Stock(models.Model):
    name = models.ForeignKey(Product, on_delete= models.PROTECT)
    type = models.CharField(max_length = 2)
    units = models.IntegerField()

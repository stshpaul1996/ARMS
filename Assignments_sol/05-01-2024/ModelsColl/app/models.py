from django.db import models
#
# # Create your models here.
#
# class Category(models.Model):
#     catogory = models.CharField(max_length=50)
#     def __repr__(self):
#         return self.catogory
# class Product(models.Model):
#     productname=models.CharField(max_length=50)
#     openingstock = models.DecimalField(max_digits=10, decimal_places=2)
#     product_unique_number = models.IntegerField()
#     def __repr__(self):
#         return self.productname
# class Cost(models.Model):
#     Cost =models.DecimalField(max_digits=10, decimal_places=2)
#     date =models.DateField()
#     def __repr__(self):
#         return self.date
#
class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Product(models.Model):
    productname = models.CharField(max_length=50)
    # openingstock = models.DecimalField(max_digits=10, decimal_places=2)
    product_unique_number = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.productname

class Cost(models.Model):
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.date)

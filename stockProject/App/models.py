from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length = 100,unique = True)

class Api(models.Model):
    name = models.CharField(max_length = 100,unique = True)

class Permissions(models.Model):
    role = models.ForeignKey(Role,on_delete = models.PROTECT)
    api = models.ForeignKey(Api,on_delete = models.PROTECT)
    has_get = models.BooleanField(default = False)
    has_post = models.BooleanField(default = False)
    has_put = models.BooleanField(default = False)
    has_delete = models.BooleanField(default = False)

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.PROTECT)
    role = models.ForeignKey(Role,on_delete = models.PROTECT)


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

class Product(models.Model):
    name = models.CharField(max_length=250)
    unique_num = models.CharField(max_length=50, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

class OpeningStock(models.Model):
    opening_stock = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

class Sales(models.Model):
    stock = models.IntegerField()
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

class Purchase(models.Model):
    stock = models.IntegerField()
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
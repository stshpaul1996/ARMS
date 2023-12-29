from django.db import models

# Create your models here.
class product_table(models.Model):
    name=models.CharField(max_length=255)
    cost_price=models.FloatField()
    profit=models.FloatField()
    discont=models.FloatField()
    mrp=models.IntegerField()
    create_date=models.DateField(auto_now_add=True)

class latest_price(models.Model):
    product_id=models.ForeignKey(Product)
    mrp=models.IntegerField()
    name=models.CharField(max_length=255)
    
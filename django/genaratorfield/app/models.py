from django.db import models
from django.db.models import F

# Create your models

class Generator(models.Model):
    name=models.CharField(max_length=25,null=True)
    costprice=models.FloatField()
    profit=models.IntegerField()
    discount=models.IntegerField()
    sellingprice = models.GeneratedField(
        expression=F("costprice") + F("profit") + F("discount"),
        output_field=models.FloatField(),
        db_persist=True,
    )
 
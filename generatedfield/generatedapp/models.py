from django.db import models
from django.db.models import F


class Square(models.Model):
    side = models.IntegerField()
    area = models.GeneratedField(
        expression=F("side") * F("side"),
        output_field=models.BigIntegerField(),
        db_persist=True,
    )


from django.db import models
from django.db.models import F

class Mrp(models.Model):
    cp = models.IntegerField()
    profit = models.IntegerField()
    discount = models.FloatField()
    MRP = models.GeneratedField(
        expression=(F("cp") + F("profit")) / (1 - F("discount")),
        output_field=models.FloatField(),
    db_persist=True
    )




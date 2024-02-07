from django.db import models

# Create your models here.
from django.db import models

class Trip(models.Model):
    name = models.CharField(max_length=100)

    

class Member(models.Model):
    name = models.CharField(max_length=100)
    trip = models.ForeignKey(Trip, related_name='members', on_delete=models.CASCADE)

    

class Expense(models.Model):
    trip = models.ForeignKey(Trip, related_name='expenses', on_delete=models.CASCADE)
    member = models.ForeignKey(Member, related_name='expenses', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    
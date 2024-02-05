from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=64)


class Student(models.Model):
    name=models.CharField(max_length=64)
    age=models.IntegerField()
    address=models.CharField(max_length=64)
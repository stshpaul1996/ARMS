from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 200)

class Employee(models.Model):
    name = models.CharField(max_length = 100)
    email_id = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete = models.PROTECT)

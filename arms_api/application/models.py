from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    salary=models.IntegerField()
    dept_id=models.ForeignKey(Department,on_delete=models.PROTECT)
    
from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=64,unique=True)
    age=models.IntegerField(null=True)
    salary=models.IntegerField(null=True)

  

class Department(models.Model):
    emp_id=models.ForeignKey(Employee,on_delete=models.PROTECT)
    department=models.CharField(null=True,max_length=64)
    location=models.CharField(null=True,max_length=64)
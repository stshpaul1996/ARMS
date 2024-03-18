from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

class Employee(Department):
    emp_name=models.CharField(max_length=100)
    emp_salary=models.IntegerField()


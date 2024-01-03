from django.db import models

# Create your models here.
<<<<<<< HEAD
class Employee(models.Model):
    name=models.CharField(max_length=64,unique=True)
    age=models.IntegerField(null=True)
    salary=models.IntegerField(null=True)

  

class Department(models.Model):
    emp_id=models.ForeignKey(Employee,on_delete=models.PROTECT)
    department=models.CharField(null=True,max_length=64)
    location=models.CharField(null=True,max_length=64)
=======
class Department(models.Model):
    dept_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    salary=models.IntegerField()
    dept_id=models.ForeignKey(Department,on_delete=models.PROTECT)
    
>>>>>>> 7cddd1a6d8b4c25cbb443e8281aa1a3452c5f16a

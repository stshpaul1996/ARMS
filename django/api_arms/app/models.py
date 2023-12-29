from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name=models.CharField(max_length=25,null=True)
    dept_location=models.CharField(max_length=50,null=True)


class Employee(models.Model):
    name=models.CharField(max_length=25,null=True)
    job_name=models.CharField(max_length=25,null=True)
    salary=models.FloatField(null=True)
    hire_date=models.DateField(null=True)
    dept_id=models.ForeignKey(Department,on_delete=models.PROTECT)





# {"name":"sharvan kumar",
# "job_name":"manager",
# "salary":"25000.00",
# "hire_date":"25-03-2023",
# "dept_id":1}
from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
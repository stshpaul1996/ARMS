from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile_no=models.IntegerField()
    location=models.CharField(max_length=100)

    # def __str__(self):
    #     return {self.id}   
class Student(models.Model):
    roll_number=models.CharField(max_length=100)
    branch=models.CharField(max_length=50)
    person_id=models.ForeignKey(Person,on_delete=models.PROTECT)
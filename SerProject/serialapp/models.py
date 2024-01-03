from django.db import models



class Student(models.Model):
    name=models.CharField(max_length=50,unique=True)
    rollno=models.IntegerField()
    age=models.IntegerField()
    
    
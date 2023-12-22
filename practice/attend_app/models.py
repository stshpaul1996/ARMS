from django.db import models
from datetime import date,time
from django.core.exceptions import ValidationError

def alpha(name):
    if name.isalpha():
        return name
    else:
        raise ValidationError('this field should contain only characters')
     




class EmployeeInfo(models.Model):
    employee_id=models.SmallIntegerField()
    first_name=models.CharField(max_length=50,validators=[alpha])
    last_name=models.CharField(max_length=50,validators=[alpha])
    email=models.EmailField(max_length=50)
    date_of_join=models.DateField(default=date.today())
    technology_id=models.IntegerField()
    mobile_no=models.IntegerField()
    file=models.ImageField(upload_to= '',null=True)
    video=models.FileField(upload_to= '',null=True)
    


class Daily_attendance(models.Model):
    employee_id=models.IntegerField()
    date=models.DateField()
    login_time=models.TimeField()
    logout_time=models.TimeField()
    status=models.CharField(max_length=50),






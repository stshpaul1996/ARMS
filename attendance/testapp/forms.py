from typing import Any
from django.db import models
from django import forms

# Create your models here.

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, validate_slug
from testapp.models import Employee

from datetime import timedelta,datetime

    

# Create your models here.
from datetime import datetime,time
def validate_phoneNum(number):
    if len(str(number)) <10:
        raise ValidationError("enter 10 digits ")
   
class Employee_Form(forms.Form):
    email_id = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=50)
    validate_phone_number = forms.IntegerField(validators=[validate_phoneNum])
    address = forms.CharField(max_length=250,validators=[validate_slug])
    tech_id = forms.IntegerField()

 
class Daily_Atendance_form(forms.Form):
    employee_id = forms.ModelChoiceField(queryset=Employee.objects.all())
    date = forms.DateField()
    check_in = forms.TimeField()
    check_out = forms.TimeField()
    #status = forms.CharField(max_length=1)

    def clean(self):

        clenaed_data = super().clean()

        t1 = clenaed_data['check_in']
        t2 = clenaed_data['check_out']

        time1 = t1.hour * 3600 + t1.minute * 60 + t1.second
        time2 = t2.hour * 3600 + t2.minute * 60 + t2.second
 
        time_diff_seconds = abs(time2 - time1)
        time_in_H = timedelta(seconds = time_diff_seconds)
        
        
        time_diff_seconds = abs(time2 - time1)
        time_in_H = timedelta(seconds = time_diff_seconds)
        if time_in_H >= timedelta(hours=9):
            clenaed_data['status'] = "P"
        else :
            clenaed_data['status'] = "A"
        return clenaed_data

 
 
# class Technology(models.Model):
#     tech_name = models.CharField(max_length=100)
 
 
# class Tech_Emp(models.Model):
#     tech = models.ForeignKey(Technology,on_delete=models.PROTECT)
#     emp = models.ForeignKey(Employee,on_delete=models.PROTECT)
 
# class Trainer(models.Model):
#     trainer_name = models.CharField(max_length = 50)
#     tech = models.ForeignKey(Technology,on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField()
 
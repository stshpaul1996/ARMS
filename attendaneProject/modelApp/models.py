
# Create your models here.

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, validate_slug
from datetime import datetime,timedelta
# Create your models here.

import datetime

def validate_name(name):
    if name.isalpha():
        return name 
    else:
        raise ValidationError("field should contain only  characters")
    
def validate_phno(number):
    if len(str(number)) ==10 and str(number)[0] in ['9','8','7','6'] and str(number).isdigit() :
        return number
    else:
        raise ValidationError("Enter valid India  phone number")


class Technology(models.Model):
    domain = models.CharField(max_length = 50,validators = [validate_name])

    def __str__(self):
        return f'{self.id}'  
    

class Employee(models.Model):
    email_id = models.EmailField(max_length=100, unique = True)
    first_name = models.CharField(max_length=20,validators = [validate_name])
    last_name = models.CharField(max_length=50,validators = [validate_name])
    validate_phone_number = models.IntegerField(unique = True,validators = [validate_phno])
    address = models.CharField(max_length=250,validators=[validate_slug])
    tech_id = models.IntegerField()

    
    
    # def __str__(self):
    #     return f'{self.id}'
    
    
    
    # def clean(self):
    #     unique_fields = ['email_id','validate_phone_number']
    #     errors = {}

    #     for field in unique_fields:
    #         field_value  = getattr(self,field)
    #         if field_value:
    #             query = Employee.objects.filter(**{field:field_value})

    #             if query.exits():
    #                 errors[field] = [f'{field} must be unique']

    #         if errors:
    #             raise ValidationError(errors)
                


        




class Daily_Atendance(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    date = models.DateField()
    check_in = models.TimeField(default = datetime.datetime.now().time())
    check_out = models.TimeField(default = datetime.datetime.now().time())
    status = models.CharField(max_length=1,blank = True)


    def calculate_time_diff(self,check_in,check_out):

        time1 = check_in.hour * 3600 + check_in.minute * 60 + check_in.second 
        time2 = check_out.hour * 3600 + check_out.minute * 60 + check_out.second 

        time_diff_seconds = abs(time2 - time1)
        return timedelta(seconds = time_diff_seconds)

    def save(self,*args,**kwargs):
        
        
        if self.check_in and self.check_out:

            time_diff = self.calculate_time_diff(self.check_in,self.check_out)
            if time_diff < timedelta(hours=9):
                self.status = "A"
            else:
                self.status = "P"
        
        super().save(*args,**kwargs)

# class Technology(models.Model):
#     domain = models.CharField(max_length = 50)

#     def __str__(self):
#         return f'{self.id}'

class Emp_Tech(models.Model):
    emp_id = models.ForeignKey(Employee,on_delete = models.DO_NOTHING)
    tech_id = models.ForeignKey(Technology,on_delete = models.DO_NOTHING)


    

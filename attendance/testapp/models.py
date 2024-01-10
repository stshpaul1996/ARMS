from django.db import models
from django.db.models import F

# Create your models here.
from datetime import datetime,timedelta

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, validate_slug
# Create your models here.


#class MyCustomField(models.CharField):
    

    # def get_prep_value(self, value):
    #     # This method is used to prepare the value for saving to the database.
    #     if value is None:
    #         return None
        
    #     #time_diff = datetime.combine(datetime.today(), self.check_out) - datetime.combine(datetime.today(), self.check_in)
        

    #     time1 = self.check_in.hour * 3600 + self.check_in.minute * 60 + self.check_in.second
    #     time2 = self.check_out.hour * 3600 + self.check_out.minute * 60 + self.check_out.second
 
    #     time_diff_seconds = abs(time2 - time1)
    #     time_in_H = timedelta(seconds = time_diff_seconds)
    #     if time_in_H >= 9:
    #          return "P"
    #     else :
    #          "A"




    
    # def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)



# def clean_status(check_in,check_out):
#         time1 = check_in.hour * 3600 + check_in.minute * 60 + check_in.second
#         time2 = check_out.hour * 3600 + check_out.minute * 60 + check_out.second
 
#         time_diff_seconds = abs(time2 - time1)
#         time_in_H = timedelta(seconds = time_diff_seconds)
        
#         time_diff_seconds = abs(time2 - time1)
#         time_in_H = timedelta(seconds = time_diff_seconds)
#         if time_in_H >= timedelta(hours=9):
#             return "P"
#         else :
#             return "A"




import datetime
def validate_phoneNum(number,last_name):
    if len(str(number)) <10:
        raise ValidationError("enter 10 digits " + last_name)
   
class Employee(models.Model):
    email_id = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    validate_phone_number = models.BigIntegerField(validators=[validate_phoneNum])
    address = models.CharField(max_length=250,validators=[validate_slug])
    tech_id = models.IntegerField()
    def __str__(self):
        return f"{self.id}"

 
class Daily_Atendance(models.Model):

    

    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField(default = datetime.datetime.now().time())
    check_out = models.TimeField()
    status = models.CharField(max_length=1)



    
    
    # status = models.GeneratedField(
    #     expression= clean_status(F('check_in'),F('check_out')),
    #     output_field=models.CharField(max_length=1),
    #     db_persist=True
    #     )

    # def clean_status(self):
    #     time1 = self.check_in.hour * 3600 + self.check_in.minute * 60 + self.check_in.second
    #     time2 = self.check_out.hour * 3600 + self.check_out.minute * 60 + self.check_out.second
 
    #     time_diff_seconds = abs(time2 - time1)
    #     time_in_H = timedelta(seconds = time_diff_seconds)
    #     return time_in_H
        
    #     # time_diff_seconds = abs(time2 - time1)
    #     # time_in_H = timedelta(seconds = time_diff_seconds)
    #     # if time_in_H >= timedelta(hours=9):
    #     #     return "P"
    #     # else :
    #     #     return "A"

    
 
class Technology(models.Model):
    tech_name = models.CharField(max_length=100)
 
 
class Tech_Emp(models.Model):
    tech = models.ForeignKey(Technology,on_delete=models.PROTECT)
    emp = models.ForeignKey(Employee,on_delete=models.PROTECT)
 
class Trainer(models.Model):
    trainer_name = models.CharField(max_length = 50)
    tech = models.ForeignKey(Technology,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
 
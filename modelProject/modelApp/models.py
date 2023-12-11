from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, validate_slug
# Create your models here.
import datetime
def validate_phoneNum(number):
    if len(str(number)) <10:
        raise ValidationError("enter 10 digits ")
class Employee(models.Model):
    email_id = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    validate_phone_number = models.SmallIntegerField(validators=[validate_phoneNum])
    address = models.CharField(max_length=250,validators=[validate_slug])
    tech_id = models.IntegerField()
class daily_Atendance(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=datetime.datetime.now())
    status = models.CharField(max_length=1)
class technology(models.Model):
    tech_name = models.CharField(max_length=100)
class tech_emp(models.Model):
    tech = models.ForeignKey(technology,on_delete=models.CASCADE)
    emp = models.ForeignKey(Employee,on_delete=models.CASCADE)

class trainer(models.Model):
    trainer_name = models.CharField(max_length = 50)
    tech = models.ForeignKey(technology,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()







































from django.db import models
from django.core.exceptions import ValidationError

def name_check(value):
    if not value.isalpha():
        raise ValidationError("Invalid Name")

def email_check(value):

    if (not value.endswith(".com") and not value.endswith(".in")):
        raise ValidationError("Invalid Email")

def phone_check(value):
    if not str(value).isdigit():
        raise ValidationError("Invalid Phone")


class Employee(models.Model):
    name = models.CharField(max_length=250, validators=[name_check], unique=True)
    email = models.EmailField(validators=[email_check])
    phone = models.IntegerField(validators=[phone_check])

class Department(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.PROTECT)
    department = models.CharField(max_length=250, validators=[name_check])
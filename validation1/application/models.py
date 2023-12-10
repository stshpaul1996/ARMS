from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
def check_negative(value):
    if value>0:
        raise Exception('expecting negative values only')
    
class NegativeIntegerField(models.IntegerField):
    default_validators=[check_negative]

class UppercaseField(models.CharField):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
    def get_prep_value(self,value):
        # prepare the value for saving to the database
        # this method is called before saving the data to the database
        return value.upper()

class Customer(models.Model):
    name=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    email=models.EmailField(max_length=100)
    aadhar=models.BigIntegerField()
    value_less_zero=NegativeIntegerField(default=-1)
    name_upper=UppercaseField(max_length=250,default="")
    min_value_id=models.SmallIntegerField(default=25,
                                          validators=[MinValueValidator(
                                              limit_value=25,
                                              message="value should greater than zero"
                                          ),])


from django.db import models

# Create your models here.

def check_negative(value):
    if value>0:
        raise Exception("expecting negative values only")

class NegativeIntegerField(models.IntegerField):
    default_validators = [check_negative]

class UpperCaseField(models.CharField):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    def get_prep_value(self, value):
            # Prepare the value for saving to the database
            # This method is called before saving the data to the database
            return value.upper()

class CustomerBase(models.Model):

    name = models.CharField(max_length=250)
    #name_upper = UpperCaseField(max_length=250, default="")
    address = models.CharField(max_length=250, default="")
    email = models.EmailField(max_length=100, default="")
    # cust_id = models.SmallIntegerField(default=0)
    # adhar = models.BigIntegerField(default=0)
    #value_less_zero = NegativeIntegerField(default=-1)
    # min_value_id = models.SmallIntegerField(default=23, 
    #                                         validators=[MinValueValidator(
    #                                             limit_value=23, 
    #                                             message="value should greater than zero"), ])


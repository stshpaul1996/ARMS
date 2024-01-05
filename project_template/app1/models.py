from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def check_spcial_symbols(value):
    print("model validation")
    if not value.isalnum():
        raise ValidationError("Expecting alpha numeric value")

class Cricketers(models.Model):
    name = models.CharField(max_length=250, validators=(check_spcial_symbols,))
    image_path = models.ImageField(max_length=250)# charField
    age = models.IntegerField(default=1)
    mobile = models.CharField(max_length=15, default="0000000000")
    created_date = models.DateTimeField(auto_now_add=True)


    def clean(self):
       # write entire instance level validation
        if self.age>18:
            if self.mobile == "0000000000":
                raise ValidationError("expecting valid mobile number")
        return super(Cricketers, self).clean()

# class Person(models.Model):
#     name = models.CharField(max_length=250)
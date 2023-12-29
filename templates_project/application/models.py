from django.db import models
from django.core.exceptions import ValidationError

def special_symbols(value):
    if not value.isalnum():
        raise ValidationError("Expecting alpha numeric values")
    
def clean(self):
        if self.age<=18 or self.mobile_number=="0000000000":
            raise ValidationError("expecting valid mobile number")
        return super(display, self).clean()

# Create your models here.
class display(models.Model):
    name=models.CharField(max_length=50,validators=[special_symbols])
    address=models.CharField(max_length=50)
    image_path=models.CharField(max_length=250)
    age=models.IntegerField(default=1)
    mobile_number=models.CharField(max_length=15,default=0000000000)

    
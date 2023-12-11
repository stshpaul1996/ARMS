from django.db import models

# Create your models here.


class EncryptionField(models.Field):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    def from_db_value(self, value, expression, connection):
            # Convert the database value to Python value
            # This method is used when retrieving data from the database
        if value is None:
             return None
        res=""
        for i in value:
            res=res+chr(ord(i)+1)
        return value    

    def get_prep_value(self, value):
         # Prepare the value for saving to the database
            # This method is called before saving the data to the database
        if value is None:
             return None
        res=""
        for i in value:
            res=res+chr(ord(i)-1)
        return value
class Customer(models.Model):
    name=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    user_name=EncryptionField()
    

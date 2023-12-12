from django.db import models

# Create your models here.
class EncryptedField(models.TextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def get_prep_value(self,value):
        encrypt=""
        for i in value:
            encrypt=encrypt+chr(ord(i)-1)
        return encrypt

    def from_db_value(self, value, expression, connection):
            # Convert the database value to Python value
            # This method is used when retrieving data from the database
        decrypt=""
        for i in value:
            decrypt=decrypt+chr(ord(i)+1)
        return decrypt

class Sample(models.Model):
    name = models.CharField(max_length=250)
    user_name = EncryptedField()
    first_name = models.CharField(max_length=10)
    
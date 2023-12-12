from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from cryptography.fernet import Fernet
from encryptionfield import settings
import re

# Create your models here.

def check_negative(value):
    if value>0:
        raise Exception("expecting negative values only")
    

class EncryptionField(models.TextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def from_db_value(self, value, expression, connection):
            # Convert the database value to Python value
            # This method is used when retrieving data from the database
            if value is not None:
                fernet = Fernet(settings.SECRET_KEY.encode('utf-8'))
                decrypted_value = fernet.decrypt(value[len('$encrypted$'):].encode('utf-8')).decode('utf-8')
                return decrypted_value
            print(value)
            return value

    # def to_python(self, value):
        
    #     if value is not None and value.startswith('$encrypted$'):
    #         fernet = Fernet(settings.SECRET_KEY.encode('utf-8'))
    #         decrypted_value = fernet.decrypt(value[len('$encrypted$'):].encode('utf-8')).decode('utf-8')
    #         return decrypted_value
    #     print(value)
    #     return value
        

    def get_prep_value(self, value):
        
        if value is not None:
            fernet = Fernet(settings.SECRET_KEY.encode('utf-8'))
            encrypted_value = fernet.encrypt(value.encode('utf-8')).decode('utf-8')
            return f'$encrypted${encrypted_value}'
        return value

class NegativeIntegerField(models.IntegerField):
    default_validators = [check_negative]

class Customer(models.Model):
    
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    cust_id = models.SmallIntegerField(default=0)
    adhar = models.BigIntegerField(default=0)
    value_less_zero = NegativeIntegerField(default=-1)
    min_value_id = models.SmallIntegerField(default=23, 
                                            validators=[MinValueValidator(
                                                limit_value=23, 
                                                message="value should greater than zero"), ])
    phoneno=models.CharField(max_length=10)
    data=EncryptionField()

def name_validator(value):
    if not value.startswith('s'):
        raise Exception('name startswith letter s')
    elif not value.endswith('r'):
        raise Exception('name endswith letter r')
    
def phone_validator(value):

    pattern = re.compile('^\+?1?[6-9]\d{9,15}$')
    if not pattern.match(value):
        raise ValidationError(
            ("Enter a valid phone number."),
            params={'value': value}
        )
    



class Student(models.Model):
    name=models.CharField(max_length=50,null=True,default='shravn',verbose_name='Name',validators=[name_validator])
    phone=models.CharField(max_length=15,null=True,default=0,verbose_name='Phone Number',validators=[phone_validator])
    email=models.EmailField(max_length=25,null=True,default='admin@gmail.com',verbose_name='Email')
    address=models.TextField(max_length=255,null=True,default='3-5,Hyderabad',verbose_name='Address')
    branch=models.CharField(max_length=25,null=True,default='EIE',verbose_name='Branch')
    year=models.CharField(max_length=20,null=True,default='1st',verbose_name='Year')
    image=models.ImageField(verbose_name='Image Upload',null=True)
    linkedin=models.URLField(verbose_name='LinkedIn',null=True,blank=True)

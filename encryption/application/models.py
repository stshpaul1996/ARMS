from django.db import models
from cryptography.fernet import Fernet
# Create your models here.
key = Fernet.generate_key()
cipher_suite=Fernet(key)

def encrypt_field(value):
    return cipher_suite.encrypt(str(value).encode())

def decrypt_field(value):
    return cipher_suite.decrypt(value).decode()

class Employee(models.Model):
    name=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    email=models.EmailField(max_length=100)
    phone_number=models.CharField(max_length=250)

    def save(self,*args,**kwargs):
        self.name=encrypt_field(self.name)
        self.address=encrypt_field(self.address)
        self.email=encrypt_field(self.email)
        self.phone_number=encrypt_field(str(self.phone_number))
        super().save(*args,**kwargs)

    def get_decrypted_name(self):
        print(decrypt_field(self.name))
    
    def get_decrypted_address(self):
        return decrypt_field(self.address)
    
    def get_decrypted_email(self):
        return decrypt_field(self.email)
    
    def get_decrypted_phone_number(self):
        return int(decrypt_field(self.phone_number))

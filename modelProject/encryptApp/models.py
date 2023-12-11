# from django.db import models
# from utils import encrypt_value, decrypt_value, generate_key

# class EncryptedField(models.TextField):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.key = generate_key()

#     def from_db_value(self, value, expression, connection):
#         if value is None:
#             return None
#         return decrypt_value(self.key, value)

#     def get_prep_value(self, value):
#         if value is None:
#             return None
#         return encrypt_value(self.key, value)

# class Student(models.Model):
#     name = models.CharField(max_length=250)
#     email = models.EmailField(max_length=100)
#     std_id = models.IntegerField(default=-1)
#     test_val = models.IntegerField(default=23)
#     enc_field = EncryptedField()

# Assuming utils.py contains necessary encryption and key generation functions
# Make sure to implement `encrypt_value`, `decrypt_value`, and `generate_key` securely in the utils module.

 

# Make sure to implement `encrypt_value`, `decrypt_value`, and `generate_key` functions securely in the my_crypto_utils module.

from django.db import models



def encrypt_value(value):
    encrypted_value =""
    for i in value:
        encrypted_value += chr(ord(i)+6)
    return encrypted_value
    

def decrypt_value(encrypted_value):
    decrypted_value = ""
    for i in encrypted_value:
        decrypted_value += chr(ord(i)-6)
    return decrypted_value

class EncryptedField(models.TextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_prep_value(self, value):
        if value is None:
            return None
        return encrypt_value(value)    

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        return decrypt_value(value)

    

class Student(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    std_id = models.IntegerField(default=-1)
    test_val = models.IntegerField(default=23)
    enc_field = EncryptedField()



 
 
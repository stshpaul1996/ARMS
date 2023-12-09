from django.db import models

def encrypt(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        encrypted_char = chr(ord(char) ^ key)
        encrypted_text += encrypted_char
    return encrypted_text

def decrypt(ciphertext, key):
    return encrypt(ciphertext, key)  # XOR encryption and decryption are the same operation

class EncryptionField(models.fields.CharField):
    def __init__(self, *args, encryption_key=0, **kwargs):
        self.encryption_key = encryption_key
        super(EncryptionField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if value is not None:
            return decrypt(value, self.encryption_key)
        return value

    def get_prep_value(self, value):
        if value is not None:
            return encrypt(value, self.encryption_key)
        return value
    
class Customer(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = EncryptionField(max_length=100, encryption_key=56, default="")
    cust_id = models.SmallIntegerField(default=0)
    adhar = models.BigIntegerField(default=0)

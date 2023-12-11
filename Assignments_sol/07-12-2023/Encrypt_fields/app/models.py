from django.db import models,connection
import string
class EencryptionField(models.CharField):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    def from_db_value(self, value, expression, connection):
        # return self.to_python(value)
        chars = ' ' + string.punctuation + string.digits + string.ascii_letters
        chars = list(chars)
        keys = ['U', '|', 'w', 'j', 'L', 'D', 'X', 'H', 'f', 'o', '!', 'b', '\\', '~', '8', 'M', 'Y', 'O', '=', ' ',
                'v',
                'n', '/', '+', 'c', 'q', 'u', 'W', 'r', 's', '{', 'J', ',', '2', '<', 'a', 'd', 'g', 'h', 'E', 'Q', ')',
                'A', '#', ':', '-', '_', '0', '"', '$', 'k', 'z', ';', '1', '?', '6', 'I', 'p', '*', '(', '`', 'l', '&',
                '^', 'Z', '}', 'K', '4', "'", '7', 'P', 'T', 'C', 'R', '.', '9', 'y', 'i', 'N', 'B', '%', '>', 'x', '3',
                '@', ']', '5', 'V', 't', 'm', 'e', 'G', '[', 'F', 'S']
        data = value
        decryp = ''
        for i in data:
            ind = keys.index(i)
            decryp += chars[ind]
        return decryp
    def get_prep_value(self, value):
        chars = ' ' + string.punctuation + string.digits + string.ascii_letters
        chars = list(chars)
        keys = ['U', '|', 'w', 'j', 'L', 'D', 'X', 'H', 'f', 'o', '!', 'b', '\\', '~', '8', 'M', 'Y', 'O', '=', ' ','v',
                'n', '/', '+', 'c', 'q', 'u', 'W', 'r', 's', '{', 'J', ',', '2', '<', 'a', 'd', 'g', 'h', 'E', 'Q', ')',
                'A', '#', ':', '-', '_', '0', '"', '$', 'k', 'z', ';', '1', '?', '6', 'I', 'p', '*', '(', '`', 'l', '&',
                '^', 'Z', '}', 'K', '4', "'", '7', 'P', 'T', 'C', 'R', '.', '9', 'y', 'i', 'N', 'B', '%', '>', 'x', '3',
                '@', ']', '5', 'V', 't', 'm', 'e', 'G', '[', 'F', 'S']
        data = value
        ency_data = ''
        for i in data:
            ind = chars.index(i)
            ency_data += keys[ind]
        return ency_data

class employee(models.Model):
    name =models.CharField(max_length=50)
    password= EencryptionField(max_length=20)
    desi =models.CharField(max_length=40)

    def __str__(self):
        return self.name

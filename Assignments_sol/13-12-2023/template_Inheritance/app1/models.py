from django.db import models

# Create your models here.
class employee(models.Model):
    name =models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    designation =models.CharField(max_length=100)
    address =models.CharField(max_length=100)
    phone_number =models.IntegerField()

    def __str__(self):
        return self.name

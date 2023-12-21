from django.db import models
from django.core.exceptions import ValidationError

def only_alp(value):
    if not value.isalpha():
        raise ValidationError('Enter the name in Alphabets only')
# Create your models here.
class Cricketer(models.Model):
    name = models.CharField(max_length = 250, validators =(only_alp,),verbose_name = 'Name')
    image_path = models.ImageField(upload_to='images/',verbose_name='Image')
    video = models.FileField(upload_to='videos/',verbose_name='Video', null=True,blank=True)


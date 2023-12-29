from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
def check_name(value):
    if not value.isalpha():
        raise ValidationError("you have to enter only alphabets")

class Medias(models.Model):
    name=models.CharField(max_length=255,validators=[check_name])
    image=models.ImageField(upload_to="media/",blank=True,null=True)
    video=models.FileField(upload_to="media/",blank=True,null=True)
    
    def __str__(self):
        return self.name
    




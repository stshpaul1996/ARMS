from django.db import models

# Create your models here.


class Cricketer(models.Model):
    name=models.CharField(max_length=25,null=True)
    age=models.IntegerField(null=True)
    phone_no=models.IntegerField(null=True)
    images=models.ImageField(upload_to='',blank=True,null=True)
    video=models.FileField(upload_to='',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)



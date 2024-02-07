from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class userPhonenumber(models.Model):
    phonenumber = models.IntegerField()

class Role(models.Model):
    name = models.CharField(max_length=100,null=True,blank = True)
class myUser(AbstractUser):
    #phonenumber = models.ForeignKey(userPhonenumber,on_delete = models.PROTECT,null = True)
    #phonenumber = models.IntegerField(null = True,default = 67886755879)
    role = models.ForeignKey(Role,on_delete = models.PROTECT, default=2)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
                
    
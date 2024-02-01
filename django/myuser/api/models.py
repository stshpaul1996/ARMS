from django.contrib.auth.models import User,AbstractUser
from django.db import models

from django.conf import settings

class UserProfileBase(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Role(UserProfileBase):
    pass

class MyUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.PROTECT,default=1)
    

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
        
class Api(UserProfileBase):
    pass
    #name = models.CharField(max_length=250, unique=True)

class Permissions(models.Model):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    api = models.ForeignKey(Api, on_delete=models.PROTECT)
    has_get = models.BooleanField(default=False)
    has_post = models.BooleanField(default=False)
    has_put = models.BooleanField(default=False)
    has_delete = models.BooleanField(default=False)



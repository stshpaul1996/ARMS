from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save



class Role(models.Model):
    name = models.CharField(max_length=100, unique=True,blank = True)

class Api(models.Model):
    name = models.CharField(max_length=250, unique=True)

class Permissions(models.Model):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    api = models.ForeignKey(Api, on_delete=models.PROTECT)
    has_get = models.BooleanField(default=False)
    has_post = models.BooleanField(default=False)
    has_put = models.BooleanField(default=False)
    has_delete = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    @receiver(post_save, sender=User)
    def user_profile_save(sender,instance,created, **kwargs):
        #import pdb;pdb.set_trace()
        if created:
            UserProfile.objects.create(user=instance, role=Role.objects.get(id=1))


from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfileBase(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Role(UserProfileBase):
    pass

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=True, blank=True)


@receiver(post_save,sender=User)
def add_role(sender,created,instance, *args,**kwargs):
    UserProfile.objects.create(user=instance,role=Role.objects.get(id=1))
        

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
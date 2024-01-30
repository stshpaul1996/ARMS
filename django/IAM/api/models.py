from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfileBase(models.Model):
    name = models.CharField(max_length=100)  # Adjust max_length based on your needs

    class Meta:
        abstract = True

class Role(UserProfileBase):
    pass

class UserProfile(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #role_inst = Role.objects.get(id=kwargs.get("role_id"))
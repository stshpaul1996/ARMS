from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)

class MyUser1(AbstractUser):

    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    
    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name='groups',
    #     blank=True,
    #     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    #     related_name="custom_user_groups",  # Changed related_name
    #     related_query_name="custom_user",   # Changed related_query_name
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name='user permissions',
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     related_name="custom_user_permissions",  # Changed related_name
    #     related_query_name="custom_user",        # Changed related_query_name
    # )
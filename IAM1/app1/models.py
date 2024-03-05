from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)

class myuser(AbstractUser):

    role = models.ForeignKey(Role, on_delete=models.PROTECT)
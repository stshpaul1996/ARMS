from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser,User

class AbstractField(models.Model):
    user_id = models.CharField(max_length = 100, unique = True)
    class Meta:
        abstract = True
    


class MyUser(AbstractField,AbstractUser):
    pass
    # User_Id = models.CharField(max_length =100 )
    
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class NameAbstractModel(models.Model):
    name=models.CharField(max_length=100,unique=True)
    class Meta:
        abstract = True

class Role(NameAbstractModel):
    pass

class MyUser(AbstractUser):
    role=models.ForeignKey(Role,on_delete=models.PROTECT)

class Api(MyUser):
    pass

class permissions(models.Model):
    role=models.ForeignKey(Role,on_delete=models.PROTECT)
    api=models.ForeignKey(Api,on_delete=models.PROTECT)
    has_get=models.BooleanField(default=False)
    has_post=models.BooleanField(default=False)
    has_put=models.BooleanField(default=False)
    has_delete=models.BooleanField(default=False)
    
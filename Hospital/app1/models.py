from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class myuser(AbstractUser):

    role = models.CharField(max_length=250)

class AbstractModel(models.Model):
    createdby = models.ForeignKey(myuser, related_name='%(class)s_created', on_delete=models.CASCADE)
    updatedby = models.ForeignKey(myuser, related_name='%(class)s_updated', on_delete=models.CASCADE)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Hospital(AbstractModel):
    name = models.CharField(max_length= 250)

class Doctor(AbstractModel):
    name = models.CharField(max_length=250)
    specialization = models.CharField(max_length=250)
    hospital =models.ForeignKey(Hospital, on_delete=models.PROTECT)

class Schedule(AbstractModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


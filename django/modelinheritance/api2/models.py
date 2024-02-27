from django.db import models
from api.models import Student
# Create your models here.


class ProxyStudentModel(Student):
    class Meta:
        proxy=True
        ordering=['name']

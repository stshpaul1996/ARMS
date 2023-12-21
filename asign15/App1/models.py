from django.db import models

# Create your models here.


class Entrepreneur(models.Model):
    name = models.CharField(max_length  =200)
    company_name = models.CharField(max_length = 100)
    img_path = models.CharField(max_length = 100)

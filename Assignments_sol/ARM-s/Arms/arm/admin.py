from django.contrib import admin
from .models import Employee,Employee_exit,Deployed,Pricipal_consultant
# Register your models here.
admin.site.register([Employee,Employee_exit,Deployed,Pricipal_consultant])
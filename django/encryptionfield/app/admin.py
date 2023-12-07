from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','email','address','cust_id','adhar','value_less_zero','min_value_id','phoneno','data']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','email','address','phone','branch','year','image','linkedin']
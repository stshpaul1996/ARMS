from django.contrib import admin
from .models import Department,Employee
# Register your models here.

@admin.register(Department)
class AdminDepartment(admin.ModelAdmin):
    list_display=['id','dept_name','dept_location']


@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display=['id','name','job_name','salary','hire_date','dept_id']
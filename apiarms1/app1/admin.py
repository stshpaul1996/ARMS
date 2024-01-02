from django.contrib import admin
from app1.models import Person,Student
# Register your models here.

@admin.register(Person)
class Person(admin.ModelAdmin):
    fields=['email',
    'mobile_no','name',
    'location']


@admin.register(Student)    
class Student(admin.ModelAdmin):
    fields=['Roll_number', 'Branch','Student_id']
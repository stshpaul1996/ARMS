from django.contrib import admin
from .models import Cricketer
# Register your models here.

@admin.register(Cricketer)
class AdminCricketer(admin.ModelAdmin):
    list_display=['name','age','phone_no','images','video','created_at']
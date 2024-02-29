from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Role

# Define a custom admin class for your MyUser model
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )

# Register your models with the custom admin classes
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Role)

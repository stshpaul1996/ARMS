from rest_framework import serializers
from . models import Api,Permission,Role,MyUser,Department,Employee

class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields ="__all__"

class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields ="__all__"

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields="__all__"

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields =['id','username','password','role']
    
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields ="__all__"
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields ="__all__"

    

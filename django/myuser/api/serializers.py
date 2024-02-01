from rest_framework import serializers
from .models import MyUser,Role,Permissions,User
class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["username","password",'email',"role"]
        extra_kwargs = {'password': {'write_only': True}}
        


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'


class Permissionsserializer(serializers.ModelSerializer):
    class Meta:
        model=Permissions
        fields='__all__'

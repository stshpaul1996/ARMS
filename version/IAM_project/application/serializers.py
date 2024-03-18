from rest_framework import serializers
from . models import Role,MyUser,Api,permissions

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=["username","password","role"]
        extra_kwargs={"password":{"write_only":True}}

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = "__all__"

class permissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = permissions
        fields = "__all__"


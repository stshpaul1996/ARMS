from rest_framework import serializers
from . models import Role,MyUser

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=["username","password","role"]
        extra_kwargs={"password":{"write_only":True}}

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"
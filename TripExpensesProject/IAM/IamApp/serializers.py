from rest_framework import serializers

from django.core.exceptions import ValidationError

from .models import *


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["username", "password", "role"]



class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = "__all__"





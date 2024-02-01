from django.contrib.auth.models import User
from app1.models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    #role = serializers.IntegerField()
    class Meta:
        model = User
        fields = ["username", "password",]


class RoleSerializer(serializers.ModelSerializer):
     class Meta:
        model = Role
        fields = ["name"]
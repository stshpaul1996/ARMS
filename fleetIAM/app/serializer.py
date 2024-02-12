from .models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model
class userPhonenumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = userPhonenumber
        fields = ['phonenumber']

class myUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = myUser
        fields = ['username','password','email','role']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"
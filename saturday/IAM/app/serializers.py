from rest_framework import serializers
from app.models import *

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields="__all__"

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=["username","password","number"]


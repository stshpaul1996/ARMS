from .models import *
from rest_framework import serializers 
from django.contrib.auth.models import User

class UserprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['aadhar','pancard','username','password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
class ParentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentModel
        fields = "__all__"

class ChildModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= ChildModel
        fields = "__all__"
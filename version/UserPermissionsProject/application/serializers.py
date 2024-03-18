from django.contrib.auth import get_user_model
from rest_framework import serializers 
from .models import Person, API,Role,Permissions

class RoleSerializer(serializers.ModelSerializer):
     class Meta:
        model = Role
        fields = ["name"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "password","email", "role"]

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = API
        fields = "__all__"

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
       # exclude = ('created_by', )

class Permissionsserializer(serializers.ModelSerializer):
    class Meta:
        model=Permissions
        fields='__all__'


        

    
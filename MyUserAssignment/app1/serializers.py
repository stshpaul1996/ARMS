from rest_framework import serializers 
from django.core.exceptions import ValidationError
from app1.models import Role, MyUser, Permissions, Api, Person


class RoleSerializer(serializers.ModelSerializer):
     class Meta:
        model = Role
        fields = ["name"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["username", "password","email", "role"]

class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = "__all__"

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


    


        

    
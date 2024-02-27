from django.contrib.auth import get_user_model
from rest_framework import serializers 
from .models import Person, Api,Role,Permissions

class RoleSerializer(serializers.ModelSerializer):
     class Meta:
        model = Role
        fields = ["id","name"]


class UserSerializer(serializers.ModelSerializer):
    #role = serializers.IntegerField()

    class Meta:
        model = get_user_model()
        fields = ["id","username", "password","email", "role"]



class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
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


        

    

from rest_framework import serializers 
from base.models import Role,User
class RoleSerializer(serializers.ModelSerializer):
     class Meta:
        model = Role
        fields = ["name"]

class UserSerializer(serializers.ModelSerializer):
    role=serializers.IntegerField()

    class Meta:
        model = User
        fields = ["username", "password","email", "role"]
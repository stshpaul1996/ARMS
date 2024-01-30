from rest_framework import serializers 
from app1.models import Role,MyUser
class RoleSerializer(serializers.ModelSerializer):
     class Meta:
        model = Role
        fields = ["name"]


class UserSerializer(serializers.ModelSerializer):
    #role = serializers.IntegerField()

    class Meta:
        model = MyUser
        fields = ["username", "password","email", "role"]
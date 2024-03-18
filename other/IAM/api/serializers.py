from rest_framework import serializers
from .models import UserProfile,Role,Permissions,User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user','role']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'


class Permissionsserializer(serializers.ModelSerializer):
    class Meta:
        model=Permissions
        fields='__all__'
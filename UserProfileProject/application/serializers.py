from rest_framework import serializers
from . models import Role,Permission,UserProfile

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields ="__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields ="__all__"

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields ="__all__"

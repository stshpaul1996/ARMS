from rest_framework import serializers
from .models import UserProfile,Role
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username','password','role']
        extra_kwargs = {'password': {'write_only': True}}


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'
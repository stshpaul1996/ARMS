from rest_framework import serializers 
from .models import MyUser1, Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role    
        fields=["name"]
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser1
        fields = ["username", "password","email", "role"]
from rest_framework import serializers
from .models import MyUser


class MyuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["username", "password", "user_id","email"]

from rest_framework import serializers
from permission_app.models import *
from django.contrib.auth import get_user_model

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields="__all__"

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=["username","password","email","role"]

class Role_serializers(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["name"]
class Api_serializers(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = "__all__"
class Permissions_serializers(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        # fields  = ["user","role_id","api_id","has_get","has_post","has_put","has_delete"]
        fields = "__all__"
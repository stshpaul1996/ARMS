from rest_framework import serializers
from django.contrib.auth.models import User
from . models import UserProfile
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password","first_name","last_name","email"]
        extra_kwargs ={"password":{"write_only":True}} #means password won't be included in the response.

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

class UserProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = UserProfile
        fields="__all__"
    
    def create(self,validated_data):
        user_data=validated_data.pop('user')
        user_serializer=UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save(password=make_password(user_serializer.validated_data['password']))
            user=user_serializer.instance
            profile=UserProfile.objects.create(user=user,**validated_data)
            return profile
        else:
            raise serializers.ValidationError(user_serializer.errors)





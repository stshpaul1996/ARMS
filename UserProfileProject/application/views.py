from django.shortcuts import render
from rest_framework import viewsets
from . models import Role,UserProfile
from django.contrib.auth.models import User
from . serializers import RoleSerializer,UserProfileSerializer
# Create your views here.

class RoleModelVieset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserProfileModelViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def create(self,serializer):
        data=serializer.data
        role_id=data.pop("role")
        user1=User.objects.create_user(**data)
        role_inst=Role.objects.get(id=role_id)
        UserProfile(user=user1,role=role_inst).save()



from django.shortcuts import render
from . serializers import MyUserSerializer,RoleSerializer
from rest_framework import viewsets
from . models import MyUser,Role
from rest_framework.response import Response
# Create your views here.
class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class =MyUserSerializer
    
    def create(self,serializer):
        data=serializer.data
        roleinst=Role.objects.get(id=serializer.data["role"])
        print(roleinst)
        data["role"]=roleinst
        print(data)
        MyUser.objects.create_user(**data)
         
class RoleModelViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class=RoleSerializer
    
    
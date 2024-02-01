from django.shortcuts import render
from rest_framework import viewsets
from app1.models import Role
from django.contrib.auth import get_user_model
from .serializers import RoleSerializer,UserSerializer

class RoleModelViewset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # import pdb; pdb.set_trace()
        data = serializer.data
        roleins = Role.objects.get(id = serializer.data['role'])
        print(roleins)
        data['role'] = roleins
        print(data)
        get_user_model().objects.create_user(**data)
           

 
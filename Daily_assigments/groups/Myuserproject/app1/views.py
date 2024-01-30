from django.shortcuts import render
from rest_framework import viewsets
from app1.models import MyUser,Role
from .serializers import RoleSerializer,UserSerializer

class RoleModelViewset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # import pdb; pdb.set_trace()
        data = serializer.data
        roleins = Role.objects.get(id = serializer.data['role'])
        print(roleins)
        data['role'] = roleins
        print(data)
        s = MyUser.objects.create_user(**data)
        s.save()   

 
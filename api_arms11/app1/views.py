from django.shortcuts import render
from rest_framework import viewsets
from .models import MyUser1, Role
from .serializer import UserSerializer, RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset=Role.objects.all()
    serializer_class=RoleSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):

    queryset = MyUser1.objects.all()
    serializer_class = UserSerializer

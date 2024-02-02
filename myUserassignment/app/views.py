from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import *

from .models import * 

class RoleViewset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer 

class MyuserViewset(viewsets.ModelViewSet):
    queryset  = MyUser.objects.all() 
    serializer_class = MyUserSerializer
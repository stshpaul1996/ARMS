from django.shortcuts import render

from rest_framework import viewsets

from .models import User, UserProfile
from .serializers import UserProfileSerializer, UserSerializer



class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
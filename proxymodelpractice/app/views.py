from django.shortcuts import render

# Create your views here.

from .models import *

from rest_framework import viewsets
from .serializers import *

class UserModelViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileModelviewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserprofileSerializer

class ParentModelviewset(viewsets.ModelViewSet):
    queryset = ParentModel.objects.all()
    serializer_class = ParentModelSerializer

class ChildModelviewset(viewsets.ModelViewSet):
    queryset = ChildModel.objects.all()
    serializer_class = ChildModelSerializer


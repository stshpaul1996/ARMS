from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import generics, mixins, views

from .models import *
from .serializers import *

class RoleModelViewset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        data = serializer.data
        role_id = data.pop("role")
        user1 = User.objects.create_user(**data)
        role_inst = Role.objects.get(id=role_id)
        UserProfile(user=user1, role=role_inst).save()
                                                             
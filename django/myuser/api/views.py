from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from .models import MyUser,Role,Permissions
from .serializers import MyUserSerializer,RoleSerializer,Permissionsserializer


    



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)

        user = MyUser.objects.create_user(**serializer.validated_data)
        print(user)
        serializer = MyUserSerializer(instance=user)
        print(instance=user)
        print(serializer)
        return Response(serializer.data)
    
class RoleModelViewset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class PermissionsModelViewset(viewsets.ModelViewSet):
    queryset = Permissions.objects.all()
    serializer_class = Permissionsserializer
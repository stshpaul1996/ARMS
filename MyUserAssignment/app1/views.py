from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics, mixins, views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.conf import settings
from django.contrib.auth import authenticate

from app1.models import Role, MyUser, Permissions, Api
from app1.serializers import UserSerializer,RoleSerializer,PermissionsSerializer, ApiSerializer
                              
import jwt

class LoginAPI(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        data = request.data
        resp_data = {"token": None, "message": ""}
        user = authenticate(**data)
        if user:
            payload = {"userId": user.id}
            resp_data["token"] = jwt.encode(payload, settings.SECRET_KEY, algorithms="HS256")
            resp_data["message"] = "OK"
            return Response(resp_data, status=status.HTTP_201_CREATED)
        
        return Response(resp_data, status=status.HTTP_401_UNAUTHORIZED)



class RoleViewset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer


class ApiViewSet(viewsets.ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
 
  
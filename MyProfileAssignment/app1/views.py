
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import generics, mixins, views

from app1.models import  Role, UserProfile
from app1.serializers import  UserSerializer, RoleSerializer

from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import jwt

# Create your views here

class LoginAPI(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        data = request.data
        resp_data = {"token":None, "message":""}
        user = authenticate(**data) #authenticate(uasername=data['username'], password=data['password'])
        if user:
            payload = {"userId": user.id}
            resp_data["token"] = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
            resp_data["message"] = "OK"
            return Response(resp_data)
        else:

            return Response(resp_data,status=status.HTTP_403_FORBIDDEN)
                              

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
       

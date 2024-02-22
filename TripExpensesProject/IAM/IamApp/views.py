from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from django.contrib.auth import authenticate
import jwt

from .models import *
from .serializers import *

class LoginAPIView(APIView):
    def post(self,request):
        data = request.data
        res = {"token":None, "msg":""}
        user = authenticate(**data)
        if user:
            payload = {"user":user.username}
            res["token"] = jwt.encode(payload,"S@tI$H", algorithm="HS256")
            res["msg"] = "OK"
            return Response(res, status=status.HTTP_201_CREATED)
        res["msg"] = "Invalid Details"
        return Response(res, status=status.HTTP_401_UNAUTHORIZED)


    
class MyUserView(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def perform_create(self, serializer):
        data = serializer.data
        role = data.pop("role")
        role_inst = Role.objects.get(id=role)
        MyUser.objects.create_user(**data, role=role_inst)


class RoleView(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class ApiView(viewsets.ModelViewSet):
    queryset = Api.objects.all()
    serializers_class = ApiSerializer


class PermissionView(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializers_class = PermissionSerializer







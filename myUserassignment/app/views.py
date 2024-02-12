from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import status
import jwt
from rest_framework.response import Response
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .models import * 
from django.contrib.auth import get_user_model

class LoginAPI(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        data = request.data
        resp_data = {"token": None, "message": ""}
        user = authenticate(**data)
        if user:
            payload = {"userId": user.id}
            resp_data["token"] = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
            resp_data["message"] = "OK"
            return Response(resp_data, status=status.HTTP_201_CREATED)
        
        return Response(resp_data, status=status.HTTP_401_UNAUTHORIZED)

class RoleViewset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer 
    # def get_queryset(self):
        
    #     return Role.objects.using('read_db').all()

    # def perform_create(self, serializer):
    #     serializer.save()

    # def perform_update(self, serializer):
    #     serializer.save()

    # def perform_destroy(self, instance):
    #     instance.delete()

class PersonModelViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # def get_queryset(self):
        
    #     return Person.objects.using('read_db').all()

    # def perform_create(self, serializer):
    #     serializer.save()

    # def perform_update(self, serializer):
    #     serializer.save()

    # def perform_destroy(self, instance):
    #     instance.delete()



class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = get_user_model().objects.all()
    serializer_class = MyUserSerializer
    
    # def get_queryset(self):
        
    #     return get_user_model().objects.using('read_db').all()

    # # def perform_create(self, serializer):
    # #     serializer.save()

    # def perform_update(self, serializer):
    #     serializer.save()

    # def perform_destroy(self, instance):
    #     instance.delete()
    def perform_create(self, serializer):
        data = serializer.data
        role_id = data.pop("role")
        role_inst = Role.objects.get(id=role_id)
        data['role'] = role_inst
        user1 = get_user_model().objects.create_user(**data)
        #serializer.save()

class ApiModelViewset(viewsets.ModelViewSet):
    queryset = API.objects.all()
    serializer_class = ApiSerializer
    # def get_queryset(self):
        
    #     return API.objects.using('read_db').all()

    # def perform_create(self, serializer):
    #     serializer.save()

    # def perform_update(self, serializer):
    #     serializer.save()

    # def perform_destroy(self, instance):
    #     instance.delete()

class permissionViewset(viewsets.ModelViewSet):
    queryset = Permissions.objects.all()
    serializer_class =permissionSerializer

    # def get_queryset(self):
        
    #     return Permissions.objects.using('read_db').all()

    # def perform_create(self, serializer):
    #     serializer.save()

    # def perform_update(self, serializer):
    #     serializer.save()

    # def perform_destroy(self, instance):
    #     instance.delete()
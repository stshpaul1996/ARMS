from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import Person, Role,API,Permissions
from .serializers import (PersonSerializer, UserSerializer,RoleSerializer, ApiSerializer,Permissionsserializer)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
import jwt
from django.conf import settings

class LoginAPIView(APIView):
    def post(self, request):
        data=request.data
        # import pdb;pdb.set_trace()
        user=authenticate(username=data.get('username'),password=data.get('password'))
        response={'jwt_token':"","status":''}
        # data['secrete_key']=settings.SECRET_KEY
        if user:
            jwt_token=jwt.encode(data,"django-insecure-+d3ma6(dx$l6@a3m=2$brygfsq4hlk809n(*s#kc3l^gm!74c4",algorithm='HS256')
            response['jwt_token']=jwt_token
            response['status']='ok'
            status_code=status.HTTP_200_OK
        else:
            response['jwt_token']="No token genarated"
            response['status']='invalid user credentials'
            status_code=status.HTTP_401_UNAUTHORIZED
        return Response(response,status=status_code)


class RoleModelViewset(viewsets.ModelViewSet):
    # authentication_classes = []
    # permission_classes = []
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class PersonModelViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ApiModelViewset(viewsets.ModelViewSet):
    # authentication_classes = []
    # permission_classes = []
    queryset = API.objects.all()
    serializer_class = ApiSerializer

class UserViewSet(viewsets.ModelViewSet):
    # authentication_classes = []
    # permission_classes = []
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
 
    def perform_create(self, serializer):
        data = serializer.data
        role_id = data.pop("role")
        role_inst = Role.objects.get(id=role_id)
        data['role'] = role_inst
        user1 = get_user_model().objects.create_user(**data)

class PermissionsViewSet(viewsets.ModelViewSet):
    queryset=Permissions.objects.all()
    serializer_class=Permissionsserializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from django.conf import settings
import jwt
from rest_framework import viewsets
from .models import UserProfile,Role
from .serializers import UserProfileSerializer,RoleSerializer

class LoginAPIView(APIView):
    def post(self, request):
        data=request.data
        
        user=authenticate(username=data.get('username'),password=data.get('password'))
        response={'jwt_token':"","status":''}
        # data['secrete_key']=settings.SECRET_KEY

        if user:
            
            jwt_token=jwt.encode(data,settings.SECRET_KEY,algorithm='HS256')
            response['jwt_token']=jwt_token
            response['status']='ok'
            status_code=status.HTTP_200_OK
        else:
            response['jwt_token']="No token genarated"
            response['status']='invalid user credentials'
            status_code=status.HTTP_401_UNAUTHORIZED

        return Response(response,status=status_code)
    



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = UserProfile.objects.create_user(**serializer.validated_data)
        serializer = UserProfileSerializer(instance=user)
        return Response(serializer.data)
    
class RoleModelViewset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
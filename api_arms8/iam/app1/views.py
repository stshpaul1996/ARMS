from django.shortcuts import render, redirect 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from django.contrib.auth import authenticate
import jwt
from django.contrib.auth.models import User
from rest_framework import viewsets
from .seri import *

# Create your views here.
class Login_api(APIView):
    def post(self, request):
        data = request.data
        # import pdb; pdb.set_trace()
        insta = {'token':None, 'message':" "}
        user = authenticate(**data)
        
        if user:
            payload = {"username":user.username}
            insta['token'] = jwt.encode(payload,'secret',algorithm="HS256")
            insta['message'] = 'Okay'
            return Response(insta)
        else:
            return Response(insta,status=status.HTTP_403_FORBIDDEN)
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


    

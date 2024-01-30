from django.shortcuts import render, redirect 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from django.contrib.auth import authenticate
from django.conf import settings
import jwt

# Create your views here.
class Login_api(APIView):

    def post(self, request):
        data = request.data
        insta = {'token':None, 'message':" "}
        user = authenticate(**data)
        
        if user:
            payload = {"hello":"hi",}
            insta['token'] = jwt.encode(payload,'secret',algorithm="HS256")
            insta['message'] = 'Okay'
            return Response(insta)
        else:
            return Response(insta,status=status.HTTP_403_FORBIDDEN)
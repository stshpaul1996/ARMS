from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_401_UNAUTHORIZED
from django.contrib.auth import authenticate
from django.conf.global_settings import SECRET_KEY
from django.conf import settings

import jwt 

class LoginApi(APIView):
    def post(self,request):
        payload = request.data 
        #import pdb;pdb.set_trace()
        print(SECRET_KEY)
        user = authenticate(username=payload.get("username"),password=payload.get("password"))

        response = {"jwt_token":"","status":""}
        status_code = HTTP_401_UNAUTHORIZED
        payload["secrete_key"] = settings.SECRET_KEY
        response["secrete_key"] = settings.SECRET_KEY

        if user:
            jwt_token = jwt.encode(payload,settings.SECRET_KEY,algorithm="HS256")
            response["jwt_token"] = jwt_token 
            response["status"] = "ok"
            status_code = HTTP_201_CREATED 
        
        return Response(response,status=status_code)
            
        





































































































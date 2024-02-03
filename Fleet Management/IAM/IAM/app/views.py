from django.shortcuts import render
from rest_framework import status
from .serializers import MyUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_401_UNAUTHORIZED
from django.contrib.auth import authenticate
from IAM.settings import SECRET_KEY

import jwt


class SignUpView(APIView):
    def post(self, request):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApi(APIView):
    def post(self, request):
        payload = request.data
        user = authenticate(username=payload.get("username"), password=payload.get("password"))
        response = {"jwt_token": "", "status": ""}
        status_code = HTTP_401_UNAUTHORIZED

        if user:
            jwt_token = jwt.encode(payload, SECRET_KEY,algorithm="HS256")
            response["jwt_token"] = jwt_token
            response["status"] = "ok"
            status_code = HTTP_201_CREATED

        return Response(response, status=status_code)

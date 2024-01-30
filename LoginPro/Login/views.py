from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.conf import settings
import jwt

class LoginView(APIView):
    def post(self, request):
        user = get_object_or_404(User, username=request.data["username"])
        if not user.check_password(request.data["password"]):
            return Response({"detail":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        payload = {"username":request.data["username"]}
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        return Response({"jwt_code":token})





class RegisterView(APIView):
    def post(self, request):
        user = UserSerializer(data=request.data)
        msg = {}
        if user.is_valid():
            user.save()
            u = User.objects.get(username=request.data["username"])
            u.set_password(request.data["password"])
            u.save()
            msg["result"] = "success"
            msg["data"] = user.data
            return Response(msg, status=status.HTTP_201_CREATED)
        return Response(user.errors)
            
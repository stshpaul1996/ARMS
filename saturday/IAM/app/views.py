from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from app.models import *
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
import jwt
from django.contrib.auth import authenticate
# Create your views here.
class Login(APIView):
   def post(self,request):
        data = request.data
        resp_data = {"token":"token not generated","message":""}
        user = authenticate(username = data['username'],password = data['password'])
        if user:
            payload = {"userName":user.username,"userId" : user.id}
            resp_data["token"] = jwt.encode(payload,settings.SECRET_KEY,algorithm="HS256")
            resp_data["message"] = "ok"
            return Response(resp_data)
        else:
            return Response(resp_data,status= status.HTTP_403_FORBIDDEN)

from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import jwt

# Create your views here.
class LoginAPI(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        data = request.data
        resp_data = {"token":None, "message":""}
        user = authenticate(**data)#authenticate(uasername=data['username'], password=data['password'])
        if user:
          
            # token_inst = Token.objects.filter(user=user)
            # if not token_inst.exists():
            #     token_inst = Token.objects.create(user=user)
            # else:
            #     token_inst = token_inst[0]
            #token_inst = Token.objects.get_or_create(user=user)[0]
            payload = {"userId": user.id}
            resp_data["token"] = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
            resp_data["message"] = "OK"
            return Response(resp_data)
        else:

            return Response(resp_data,status=status.HTTP_403_FORBIDDEN)



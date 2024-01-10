from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class LoginAPI(APIView):
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
            token_inst = Token.objects.get_or_create(user=user)[0]
            resp_data["token"] = token_inst.key
            resp_data["message"] = "OK"
            return Response(resp_data)
        else:

            return Response(resp_data,status=status.HTTP_403_FORBIDDEN)



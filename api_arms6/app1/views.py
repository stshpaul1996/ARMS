from django.shortcuts import render
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate 
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
class login_view(APIView):
    def post(self, request):
        tk = {'token': None, 'Message': " "}
        data = request.data
        user = authenticate(**data)
        if user:
            tk1 = Token.objects.get_or_create(user=user)[0]
            tk['token'] = tk1.key
            tk['Message'] = 'Okay.'

            return Response(tk)
        else:
            return Response(tk, status=status.HTTP_401_UNAUTHORIZED)


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response
from .models import *
from .seri import Persons
from .auth256 import JWTAuth
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class Personv(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        p = Persons(data=request.data)
        mess = ''
        if p.is_valid():
            p.save()
            mess = "data is saved"
            hello = status.HTTP_201_CREATED
        else:
            mess = "data is not saved"
            hello = status.HTTP_400_BAD_REQUEST
        return Response(mess, hello)

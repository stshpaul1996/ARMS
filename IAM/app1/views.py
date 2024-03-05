from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import jwt
from django.contrib.auth import authenticate

# Create your views here.
class IAM(APIView):
    def post(self, request):
        data = request.data
        mess = {'Token':None, 'message':''}
        user = authenticate(**data)

        if user:
            payload={'username':user.username}
            mess['Token']=jwt.encode(payload,'crazy',algorithm='HS256')
            mess['message']='OKAY'
            return Response(mess,status.HTTP_201_CREATED)
        else:
            return Response(mess,status.HTTP_403_FORBIDDEN)



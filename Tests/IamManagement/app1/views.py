from django.shortcuts import render
   
from rest_framework.response import Response
from rest_framework import status,viewsets
from django.contrib.auth import authenticate
import jwt
from django.conf import settings
from rest_framework.views import APIView
import jwt
from .serializers import MyuserSerializer
from django.contrib.auth import get_user_model


class UserCreation(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = MyuserSerializer

    def perform_create(self, serializer):
        # import pdb; pdb.set_trace()               
        data = serializer.data
        get_user_model().objects.create_user(**data)
           
 
class LoginApi(APIView):
    authentication_classes=[]
    permission_classes=[]
 
    def post(self,request):
        data=request.data
        rel_data={'token':None,'msg':''}
        
        user =authenticate(**data)
        if user:
            jtoken=jwt.encode(data,settings.SECRET_KEY,algorithm='HS256')
            rel_data['token']=jtoken
            rel_data["msg"]='token generated'
            return Response(rel_data)
        else:
            return Response(rel_data,status=status.HTTP_403_FORBIDDEN)
         




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.conf import settings
import jwt

# Create your views here.
class LoginApi(APIView):
    authentication_class = []
    permission_classes=[]
    
    def post(self, request, *args, **kwargs):
        data=request.data
        rel_data={"token":None,"msg":""}
        user=authenticate(**data)
        
        if user:
            jtoken=jwt.encode(data,settings.SECRET_KEY,algorithm='HS256')
            rel_data['token']=jtoken
            rel_data['msg']="token generated"
            return Response(rel_data)
        else:
            return Response(rel_data,status=status.HTTP_403_FORBIDDEN)

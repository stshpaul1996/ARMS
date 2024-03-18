from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
import jwt

# Create your views here.
class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data=request.data
        res={"token":None,"msg":""}
        user=authenticate(**data)
        if user:
            payload={"user":user.username}
            res["token"]=jwt.encode(payload,"Bh@g@v@@n", algorithm="HS256")
            res["msg"]="ok"
            return Response(res,status=status.HTTP_201_CREATED)
        res["msg"]="Invalid details"
        return Response(res,status=status.HTTP_401_UNAUTHORIZED)
    


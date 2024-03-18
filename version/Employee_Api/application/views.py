from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
import jwt
from django.contrib.auth.models import User
from . serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self,serializer):
        data=serializer.data
        User.objects.create_user(**data)


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data=request.data
        res={"token":None,"msg":""}
        user=authenticate(**data)
        if user:
            payload={"user":user.username}
            res["token"]=jwt.encode(payload,"bhagavaan", algorithm="HS256")
            res["msg"]="ok"
            return Response(res,status=status.HTTP_201_CREATED)
        res["msg"]="Invalid details"
        return Response(res,status=status.HTTP_401_UNAUTHORIZED)
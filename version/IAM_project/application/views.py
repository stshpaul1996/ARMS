from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_401_UNAUTHORIZED
from django.contrib.auth import authenticate
from django.conf.global_settings import SECRET_KEY
from django.conf import settings
from datetime import datetime, timedelta
from rest_framework import viewsets
from . models import Role,MyUser,Api,permissions
import jwt
from . serializers import MyUserSerializer,RoleSerializer,ApiSerializer,permissionsSerializer

class MyUserView(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class RoleView(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class ApiView(viewsets.ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer 

class PermissionsView(viewsets.ModelViewSet):
    queryset = permissions.objects.all()
    serializer_class = permissionsSerializer 
 
class LoginApi(APIView):
    def post(self,request):
        payload = request.data
        #import pdb;pdb.set_trace()
        #print(SECRET_KEY)
        #user = authenticate(username=payload.get("username"),password=payload.get("password"))
        user = authenticate(**payload)
        print(user,"dfjdslfjsfjalfajfs")
        response = {"jwt_token":"","status":""}
        status_code = HTTP_401_UNAUTHORIZED
        
        if user:
            payload["user_id"] = user.id
            print(payload)
            payload["exp"] = datetime.utcnow() + timedelta(seconds=settings.JWT_EXPIRY_MINUTES)
            print(payload)
            jwt_token = jwt.encode(payload,settings.SECRET_KEY,algorithm="HS256")
            response["jwt_token"] = jwt_token
            response["status"] = "ok"
            status_code = HTTP_201_CREATED
        return Response(response,status=status_code)
 
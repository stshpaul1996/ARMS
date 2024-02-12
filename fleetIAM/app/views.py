from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.conf.global_settings import SECRET_KEY
from django.conf import settings
from datetime import datetime, timedelta
import jwt 


class LoginApi(APIView):
    # def post(self,request):
        #import pdb;pdb.set_trace()
        # payload = request.data 
        # user = authenticate(**payload)
        # #username=payload.get('username'),password=payload.get('password')
    
        # response = {"jwt_token":"","status":""}
        # status_code = HTTP_401_UNAUTHORIZED
        # print(user)
        # #payload["exp"] = datetime.utcnow() + timedelta(seconds=settings.JWT_EXPIRY_MINUTES)
        # if user:
        #     #import pdb;pdb.set_trace()
        #     payload['id'] = user.id
        #     payload['role_id'] = user.role_id
        #     jwt_token = jwt.encode(payload,settings.SECRET_KEY,algorithm="HS256")
        #     response["jwt_token"] = jwt_token 
        #     response["status"] = "ok"
        #     status_code = HTTP_201_CREATED 
        
        # return Response(response,status=status_code)
       
    def post(self, request):
        data = request.data
        import pdb;pdb.set_trace()
        resp_data = {"token": None, "message": ""}
        user = authenticate(**data)
        if user:
            payload = {"userId": user.id}
            resp_data["token"] = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
            resp_data["message"] = "OK"
            return Response(resp_data, status=status.HTTP_201_CREATED)
        
        return Response(resp_data, status=status.HTTP_401_UNAUTHORIZED)
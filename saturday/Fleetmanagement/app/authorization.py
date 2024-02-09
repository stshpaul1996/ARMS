from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework import exceptions
import jwt
# class MyAuthentication(BaseAuthentication):
#     def authenticate(self, request):
        
#         return super().authenticate(request)

class JWTAuth(TokenAuthentication):
   def authenticate_credentials(self, key):
        # print(key,"jjjjjjjjjjj")
        try:
            payload=jwt.decode(key,settings.SECRET_KEY ,algorithms="HS256")
            # print(payload,"kkkkkkkkkkkkkk")
            user_inst=User.objects.get(pk=payload.get("userId"))
            # print(user_inst,"llllllllllllll")
        except Exception as err:
            raise exceptions.AuthenticationFailed("Invalid token99999")
        if not user_inst.is_active:
            raise exceptions.AuthenticationFailed("User inactive or deleted")
        return (user_inst,key)
   
   

   
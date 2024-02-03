
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from rest_framework import settings
import pdb
 
class MyAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):
        print(key)
        IamManagementSecret = "django-insecure-9k#+&5n#qmw@p$oll=eps_h!y7u07ves5fy3r5l2z=!v7h*e0f"

        try:
            user =jwt.decode(key,IamManagementSecret,algorithms='HS256')
            print(user)
            user_instance=User.objects.filter(username=user['username'])
            print(user_instance)
 
        except Exception as err:
            raise exceptions.AuthenticationFailed('invalid token')
        if not user_instance.is_active:
            raise exceptions.AuthenticationFailed('user not available')
        return(user_instance,key)
 
 
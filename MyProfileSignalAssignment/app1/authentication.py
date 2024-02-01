from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework import exceptions
import jwt

class JWTAuth(TokenAuthentication):
 
    def authenticate_credentials(self, key):    
        try:
            payload = jwt.decode(key, settings.SECRET_KEY, algorithms="HS256")
            user_inst = User.objects.get(pk=payload.get("userId"))
        except Exception as err:
            raise exceptions.AuthenticationFailed('Invalid token.')

        if not user_inst.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return (user_inst, key)

# from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
import jwt
from .models import myuser
class JWTAuth(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            payload = jwt.decode(key,'crazy',algorithms="HS256")
            # Create a simple user object
            user = myuser.objects.get_or_create(username=payload['username'],role=payload['role'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired.')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token.')

        return (user, key)

        

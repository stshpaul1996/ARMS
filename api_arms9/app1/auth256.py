# from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
import jwt

class SimpleUser:
    def __init__(self, token):
        self.token = token
        self.is_authenticated = True
        self.is_active = True
        # Add other necessary attributes and methods if needed

# Your JWTAuth class
class JWTAuth(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            payload = jwt.decode(key, 'secret', algorithms="HS256")
            # Create a simple user object
            user = SimpleUser(token=key)
            print(user)

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired.')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token.')

        return (user, key)

        

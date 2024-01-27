from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
import jwt

class JWTAuth(TokenAuthentication):

    def authenticate_credentials(self, key):
        try:
            print('hello1')
            payload1 = jwt.decode(key,'secret', algorithm="HS256")
            print('hello2')
            user_inst = User.objects.get(pk=payload1.get("username"))

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired.')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token.')
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user.')

        if not user_inst.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return (user_inst, key)

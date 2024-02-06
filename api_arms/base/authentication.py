from django.conf import settings
#from django.contrib.auth.models import User
from app1.models import MyUser


from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.permissions import BasePermission
from rest_framework import exceptions
import jwt
class JWTAuth(TokenAuthentication):
    # def authenticate(self, request):
    #     auth = get_authorization_header(request).split()
    #     import pdb;pdb.set_trace()
    #     print("hello")

    def authenticate_credentials(self, key):    
        try:
            payload = jwt.decode(key, settings.SECRET_KEY, algorithm="HS256")
            user_inst = MyUser.objects.get(pk=payload.get("userId"))
        except Exception as err:
            raise exceptions.AuthenticationFailed('Invalid token.')

        if not user_inst.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return (user_inst, key)
    
class CheckPermission(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        given_api = request.META["PATH_INFO"]
        role_inst = request.user.role
        if given_api=="/person/":
            pass
        else:
            return bool(request.user and request.user.is_authenticated)



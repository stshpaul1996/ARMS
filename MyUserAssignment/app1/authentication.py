from django.conf import settings
from app1.models import MyUser

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission
from rest_framework import exceptions
from .models import *

import jwt

class JWTAuth(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            payload = jwt.decode(key, settings.SECRET_KEY, algorithms="HS256")
            user_inst = MyUser.objects.get(pk=payload.get("userId"))
        except Exception as err:
            raise exceptions.AuthenticationFailed("Invalid token.")
        
        if not user_inst.is_active:
            raise exceptions.AuthenticationFailed("User inactive or deleted")
        
        return (user_inst, key)


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        give_api = request.META["PATH_INFO"]
        get_api = Api.objects.get(name=give_api)
        role_id = request.user.role.id
        get_permissions = Permissions.objects.get(role=role_id, api=get_api.id)  

        methods = {
            "GET": get_permissions.has_get,
            "POST": get_permissions.has_post,
            "PUT": get_permissions.has_put,
            "DELETE": get_permissions.has_delete

        }    
       
        if methods[request.method]:
            return True
        
        return False

        
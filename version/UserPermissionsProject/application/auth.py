
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext as _
import jwt
from rest_framework.permissions import BasePermission
from .models import API,Permissions,MyUser

class CustomAuthentication(TokenAuthentication):
    def authenticate_credentials(self,key):
        # import pdb; pdb.set_trace()
        
        try:
            user=jwt.decode(key,"django-insecure-+d3ma6(dx$l6@a3m=2$brygfsq4hlk809n(*s#kc3l^gm!74c4",algorithms='HS256')
            user_inst=MyUser.objects.get(username=user['username'])
        except Exception as err:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))
        if not user_inst.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
        return(user_inst,key)
    
class CheckPermission(BasePermission):
     def has_permission(self, request, view):
        # import pdb;pdb.set_trace()
        given_api = request.META["PATH_INFO"]
        print(given_api)
        role_id = request.user.role.id
        print(role_id)
        user_id = request.user.id
        apis = API.objects.get(name=given_api)
        print(apis)
        permissions = Permissions.objects.get(role_id=role_id,api_id=apis.id)
        dic = {"GET":permissions.has_get,"POST":permissions.has_post,"PUT":permissions.has_put,"DELETE":permissions.has_delete}
        is_have_permision = dic[request.method]
        if is_have_permision:
            return bool(request.user and request.user.is_authenticated)
        else :
            return False
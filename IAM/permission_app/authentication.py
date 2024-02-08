
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate, get_user_model
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import jwt
from permission_app.models import *
from django.conf import settings
from rest_framework.permissions import BasePermission
from rest_framework import HTTP_HEADER_ENCODING, exceptions

class CustomAuthentication(TokenAuthentication):
   
    def authenticate_credentials(self, key):
        # import pdb;pdb.set_trace()
        model = self.get_model()
        try:
            #token = model.objects.select_related('user').get(key=key)
            user = jwt.decode(key,settings.SECRET_KEY,algorithms="HS256")
            usr_inst = get_user_model().objects.get(id=user["userId"])
        
        except Exception as err:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))
 
       
 
        except jwt.ExpiredSignatureError:
            return None
 
        return (usr_inst, key)
    def get_token_from_header(self, request):
        header = request.headers.get("Authorization")
        if header and header.startswith("Token "):
            return header.split(" ")[1]
        return None
 
   
 
class CheckPermission(BasePermission):
     
     
     def has_permission(self, request, view):
        # import pdb;pdb.set_trace()
        given_api = request.META["PATH_INFO"]
        role_id = request.user.role.id
        user_id = request.user.id
        apis = Api.objects.get(name=given_api)
        permissions = Permissions.objects.get(user_id=user_id, role_id_id=role_id,api_id_id=apis.id)
        print(permissions,'===========================================')
        dic = {"GET":permissions.has_get,"POST":permissions.has_post,"PUT":permissions.has_put,"DELETE":permissions.has_delete}
       
        is_have_permision = dic[request.method]
       
        if is_have_permision:
               
            return bool(request.user and request.user.is_authenticated)
        else :
            return False
       
       
 
 
 
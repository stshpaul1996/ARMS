from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from django.conf import settings
import jwt
from rest_framework import exceptions
from arms.models import Api,Permission
class JwtAuth(TokenAuthentication):
    def authenticate_credentials(self, key):
        # import pdb ; pdb.set_trace()
        
        try:
            payload = jwt.decode(key, "secret", algorithms="HS256")
            user_inst = get_user_model().objects.get(pk = payload.get("userId"))
        
            # token = model.objects.select_related('user').get(key=key)
        except Exception as err:
            raise exceptions.AuthenticationFailed('Invalid token.')
            
        if not user_inst.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')
        
        return (user_inst, key)

class CheckPermission(BasePermission):
     
     
     def has_permission(self, request, view):
        # import pdb;pdb.set_trace()
        given_api = request.META["PATH_INFO"]
        role_id = request.user.role.id
        user_id = request.user.id
        apis = Api.objects.get(name=given_api)
        permissions = Permission.objects.get(user_id_id=user_id, role_id=role_id,api_id=apis.id)
        dic = {"GET":permissions.has_get,"POST":permissions.has_post,"PUT":permissions.has_put,"DELETE":permissions.has_delete}
    
        is_have_permision = dic[request.method]
       
        if is_have_permision:
               
            return bool(request.user and request.user.is_authenticated)
        else :
            return False 
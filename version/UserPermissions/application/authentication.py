from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
import jwt
from . models import Api,Permission,MyUser
from rest_framework.permissions import BasePermission


class JWTAuth(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            payload = jwt.decode(key, "Bh@g@v@@n",  algorithms="HS256")
        except Exception as err:
            raise exceptions.AuthenticationFailed("Invalid Token")
        return (payload, key)

class CustomPermission(BasePermission):
    def has_permission(self,request,view):
        given_api=request.META.get("PATH_INFO")
        c=0
        path=""
        for i in given_api:
            path +=i
            if i=="/":
                c +=1
            if c==2:
                break
        # import pdb;pdb.set_trace()
        get_api=Api.objects.get(name=path)
        # import pdb;pdb.set_trace()


        user=MyUser.objects.get(username=request.user["username"])
        role_id=user.role_id
        get_permissions=Permission.objects.get(role=role_id,api=get_api.id)
        methods={
            "GET":get_permissions.has_get,
            "POST":get_permissions.has_post,
            "PUT":get_permissions.has_put,
            "DELETE":get_permissions.has_delete
        }
        if given_api.startswith(str(get_api.name)) and methods[request.method]:
            return True
        return False
from rest_framework.authentication import BaseAuthentication,TokenAuthentication
from django.conf import settings
import jwt
from rest_framework.exceptions import AuthenticationFailed
import uuid
from rest_framework.permissions import BasePermission
from .models import *

        
class jwtAuthentication(TokenAuthentication):
   
    def authenticate_credentials(self, key):
        #import pdb;pdb.set_trace()
        model = self.get_model()
        try:
            #token = model.objects.select_related('user').get(key=key)
            user = jwt.decode(key,"django-insecure-7ag3aue)q^+7xy1zrhvpxxv=us84=_@u^=nw+d3c6-jxhveh6u",algorithms="HS256")
            #usr_inst = User.objects.get(username=user["username"])
            user['is_authenticated'] = True
        except Exception as err:
            raise AuthenticationFailed('Invalid token.')
 
       
        except jwt.ExpiredSignatureError:
            return None
 
        return (user, key)
    def get_token_from_header(self, request):
        header = request.headers.get("Authorization")
        if header and header.startswith("Token "):
            return header.split(" ")[1]
        return None

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        give_api = request.META["PATH_INFO"]
        get_api = API.objects.get(name=give_api)
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
        




















    #  def has_permission(self, request, view):

    #     #import pdb;pdb.set_trace()

    #     given_api = request.META["PATH_INFO"]

    #     role_id = request.user.role.id

    #     user_id = request.user.id

    #     apis = API.objects.get(name=given_api)

    #     permissions = Permissions.objects.get(role_id_id=role_id,api_id_id=apis.id)

    #     dic = {"GET":permissions.has_get,"POST":permissions.has_post,"PUT":permissions.has_put,"DELETE":permissions.has_delete}

       

    #     is_have_permision = dic[request.method]

       

    #     if is_have_permision:

               

    #         return bool(request.user and request.user.is_authenticated)

    #     else :

    #         return False

    # fleet/authentication.py

# import jwt
# from datetime import datetime, timedelta
# from django.conf import settings
# from rest_framework.authentication import BaseAuthentication
# from rest_framework.exceptions import AuthenticationFailed
# from iam.models import MyUser  

# class jwtAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         token = request.headers.get('Authorization', '').split(' ')[1] 
#         if not token:
#             return None
        
#         try:
#             decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
#             username = decoded_token.get('username')
#             if username:
#                 user = MyUser.objects.get(username=username)
#                 return (user, None)
#             else:
#                 raise AuthenticationFailed('Invalid token')p
#         except jwt.ExpiredSignatureError
    
#             raise AuthenticationFailed('Token has expired')
#         except jwt.DecodeError:
#             raise AuthenticationFailed('Invalid token')
#         except MyUser.DoesNotExist:
#             raise AuthenticationFailed('User not found')
# class jwtAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         token = request.headers.get('Authorization', '').split(' ')[1]  # Assuming token format is 'Bearer <token>'
#         if not token:
#             return None
        
#         try:
#             decoded_token = jwt.decode(token, "django-insecure-7ag3aue)q^+7xy1zrhvpxxv=us84=_@u^=nw+d3c6-jxhveh6u", algorithms=['HS256'])
#             username = decoded_token.get('username')
#             if username is not None:
#                 return (username, None)
#             else:
#                 raise AuthenticationFailed('Invalid token')
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Token has expired')
#         except jwt.DecodeError:
#             raise AuthenticationFailed('Invalid token')
from rest_framework.authentication import BaseAuthentication,TokenAuthentication
from django.conf import settings
import jwt
from rest_framework.exceptions import AuthenticationFailed
import uuid

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
        
class jwtAuthentication(TokenAuthentication):
   
    def authenticate_credentials(self, key):
        #import pdb;pdb.set_trace()
        model = self.get_model()
        try:
            #token = model.objects.select_related('user').get(key=key)
            user = jwt.decode(key,"django-insecure-7ag3aue)q^+7xy1zrhvpxxv=us84=_@u^=nw+d3c6-jxhveh6u",algorithms="HS256")
            #import pdb;pdb.set_trace()
            #usr_inst = User.objects.get(username=user["username"])
            user['is_authenticated'] = True
           # user_id = user.get('user_id')
            #return(user_id,None)
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
#                 raise AuthenticationFailed('Invalid token')
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Token has expired')
#         except jwt.DecodeError:
#             raise AuthenticationFailed('Invalid token')
#         except MyUser.DoesNotExist:
#             raise AuthenticationFailed('User not found')

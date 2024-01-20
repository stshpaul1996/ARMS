from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate, get_user_model
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import jwt

from rest_framework import HTTP_HEADER_ENCODING, exceptions

def get_authorization_header(request):
    """
    Return request's 'Authorization:' header, as a bytestring.

    Hide some test client ickyness where the header can be unicode.
    """
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, str):
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth


class CustomAuthentication(TokenAuthentication):
    """
    Simple token based authentication.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:

        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """

    keyword = 'Token'
    model = None

    def get_model(self):
        if self.model is not None:
            return self.model
        from rest_framework.authtoken.models import Token
        return Token

    """
    A custom token model may be used, but must have the following properties.

    * key -- The string identifying the token
    * user -- The user to which the token belongs
    """

    # def authenticate(self, request):
    #     #import pdb;pdb.set_trace()
    #     # print(request.data)
    #     # print(dir(request))
    #     # request.META

    #     # print(request.headers)
       
    #     # #import pdb;pdb.set_trace()
    #     # response = {"data":None,"status":''}
        
    #     # data = request.data
    #     # print(data)
    #     # #person = User.objects.filter(username=data.get("username"),password=data.get("password"))
    #     # is_authenticated = authenticate(username=data.get("username"),password=data.get("password"))
    #     # print(is_authenticated)
    #     # if is_authenticated:
    #     #     payload = request.data
    #     #     #token = Token.objects.get_or_create(user = is_authenticated)[0]
    #     #     token = jwt.encode(payload,"#^dhejh",algorithm="HS256")
    #     #     #response["data"] = token.key
    #     #     response["data"] = token
    #     #     response["status"] = "ok"
            
        
        
    #     token =    get_authorization_header(request).split()[1].decode()
    #     user = ""

    #     if token:
    #         print(token)
    #         user = jwt.decode(token,"#^dhejh",algorithms="HS256")
    #         user = jwt.decode(token,"#^dhejh",algorithms="HS256")
        

    #     return user
    def authenticate_credentials(self, key):
        #import pdb;pdb.set_trace()
        model = self.get_model()
        try:
            #token = model.objects.select_related('user').get(key=key)
            user = jwt.decode(key,"#^dhejh",algorithms="HS256")
            usr_inst = User.objects.get(username=user["username"])
        except Exception as err:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not usr_inst.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (usr_inst, key)

    def authenticate_header(self, request):
        return self.keyword

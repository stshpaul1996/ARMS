from rest_framework.authentication import TokenAuthentication
import jwt
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from fleet_management.settings import SECRET_KEY
from django.utils.translation import gettext_lazy as _


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
    keyword = 'Token'
    model = None

    def get_model(self):
        if self.model is not None:
            return self.model
        from rest_framework.authtoken.models import Token
        return Token
    def authenticate_credentials(self, key):
        try:
            user = jwt.decode(key,SECRET_KEY,algorithms="HS256")
            # print(user["username"])
            # usr_inst = User.objects.get(username=user["username"])

        except Exception as err:
            print(err)
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        # if not usr_inst.is_active:
        #     raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (user, key)

    def authenticate_header(self, request):
        return self.keyword
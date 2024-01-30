
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
import jwt

# class CustomAuthToken(ObtainAuthToken):
#  def post(self, request, *args, **kwargs):
#   serializer = self.serializer_class(data=request.data, context={'request': request})
#   serializer.is_valid(raise_exception=True)
#   user = serializer.validated_data['user']
#   token, created = Token.objects.get_or_create(user=user)
#   return Response({
#     'token': token.key,
#      'user_id': user.pk,
#      'email': user.email
#   })


class CustomAuthentication(TokenAuthentication):
    def authenticate_credentials(self,key):
        model=self.get_model()
        try:
            user=jwt.decode(key,'django-insecure-s@2czm^0zc!p1qq=w878&f$n^62*t+n050g#b=j&7a^$nv+%!6',algorithms='HS256')
            user_inst=User.objects.get(username=user['username'])
        except Exception as err:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))
        if not user_inst.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
        return(user_inst,key)
    
    def authenticate_header(self,request):
        return self.keyword
#from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import BaseAuthentication
from django.conf import settings
import jwt

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = self.get_token_from_header(request)
        if not token:
            return None

        try:
            decoded_token = jwt.decode(token,"django-insecure-p$j^7!^((g_1+raun_-93t+kw_b$p262f5vb=wd2vo#d*b()1#", algorithms=["HS256"])
            # You can perform additional validation or retrieve user data from the token payload here
            username = decoded_token["username"]
            # Fetch user from the database using the username if required
            # user = User.objects.get(username=username)
            return (username, None)
        except jwt.ExpiredSignatureError:
            return None

    def get_token_from_header(self, request):
        header = request.headers.get("Authorization")
        if header and header.startswith("Token "):
            return header.split(" ")[1]
        return None



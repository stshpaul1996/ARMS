from rest_framework.authentication import BaseAuthentication
from django.conf import settings
import jwt

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token=self.get_token_from_header(request)
        if not token:
            return None
        try:
            decoded_token=jwt.decode(token,"django-insecure-&1+v)01me#-%t67x17_)4o--fe7&4&en&0tk(!o-z881h9_j5=",algorithms=["HS256"])
            username=decoded_token["username"]
            return (username,None)
        except jwt.ExpiredSignatureError:
            return None
        
    def get_token_from_header(self, request):
        header=request.headers.get("Authorization")
        if header and header.startswith("Token"):
            return header.split(" ")[1]
        return None
    
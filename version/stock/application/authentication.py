from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
import jwt
users = {}

class JWTAuth(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            payload = jwt.decode(key, "Bh@g@v@@n",  algorithms="HS256")
            users["user"] = payload["user"]
            
        except Exception as err:
            raise exceptions.AuthenticationFailed("Invalid Token")
       
        return (payload, key)
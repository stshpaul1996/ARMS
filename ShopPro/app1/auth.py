from rest_framework.authentication import TokenAuthentication

class CustomAuthentication(TokenAuthentication):
    def authenticate(self, request):
        pass

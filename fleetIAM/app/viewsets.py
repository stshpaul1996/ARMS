from .models import *
from .serializer import * 
from rest_framework import viewsets 

class myUserViewset(viewsets.ModelViewSet):
    queryset = myUser.objects.all()
    serializer_class = myUserSerializer

class userPhonenumberViewset(viewsets.ModelViewSet):
    queryset = userPhonenumber.objects.all()
    serializer_class = userPhonenumberSerializer
    def perform_create(self, serializer):
        data = serializer.data
        role_id = data.pop("role")
        role_inst = Role.objects.get(id=role_id)
        user = myUser.objects.create_user(**data,role=role_inst)

class RoleViewswet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
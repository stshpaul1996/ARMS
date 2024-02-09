from rest_framework import viewsets 
from app.models import *
from app.serializers import *

class PersonViewSet(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer 

class MyUserViewSet(viewsets.ModelViewSet):
    queryset=MyUser.objects.all()
    serializer_class=MyUserSerializer


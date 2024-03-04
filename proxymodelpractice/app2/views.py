# app2/views.py
from rest_framework import viewsets 
from .models import *
from .serializers import *

class ProxymodelViewSet(viewsets.ModelViewSet):
    queryset = Proxymodel.objects.all()
    serializer_class = Proxyserializer
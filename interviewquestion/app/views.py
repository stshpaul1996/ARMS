from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import viewsets
class DetailsViewset(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer
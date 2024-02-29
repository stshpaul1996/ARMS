from django.shortcuts import render

from rest_framework import viewsets
from .models import ProxyUserProfile, Visits
from .serializers import ProxySerializer, VisitsSerializer

# Create your views here.

class ProxyView(viewsets.ModelViewSet):
    queryset = ProxyUserProfile.objects.all()
    serializer_class = ProxySerializer


class VisitsView(viewsets.ModelViewSet):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer
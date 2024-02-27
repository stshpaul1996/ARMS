from django.shortcuts import render
from rest_framework import viewsets
from .models import ProxyStudentModel
from .serializers import ProxyStudentSerializer
# Create your views here.


class ProxyViewsets(viewsets.ModelViewSet):
    queryset=ProxyStudentModel.objects.all()
    serializer_class=ProxyStudentSerializer
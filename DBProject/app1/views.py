from django.shortcuts import render

from rest_framework import viewsets


from .serializers import *
from .models import *

# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
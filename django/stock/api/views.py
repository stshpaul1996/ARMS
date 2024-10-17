from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class CustomerViewsets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewsets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PurchaseViewsets(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class SalesViewsets(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

class PurchaseorderViewsets(viewsets.ModelViewSet):
    queryset = Purchaseorder.objects.all()
    serializer_class = PurchaseorderSerializer
    

class SalesorderViewsets(viewsets.ModelViewSet):
    queryset = Salesorder.objects.all()
    serializer_class = SalesorderSerializer
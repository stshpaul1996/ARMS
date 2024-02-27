from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class CustomerViewsets(viewsets.Modelviewsets):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewsets(viewsets.Modelviewsets):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PurchaseViewsets(viewsets.Modelviewsets):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class SalesViewsets(viewsets.Modelviewsets):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

class PurchaseorderViewsets(viewsets.Modelviewsets):
    queryset = Purchaseorder.objects.all()
    serializer_class = PurchaseorderSerializer

class salesorderViewsets(viewsets.Modelviewsets):
    queryset = Salesorder.objects.all()
    serializer_class = SalesorderSerializer
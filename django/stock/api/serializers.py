from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Purchase
        fields='__all__'


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sales
        fields='__all__'

class PurchaseorderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Purchaseorder
        fields='__all__'

class SalesorderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Salesorder
        fields='__all__'
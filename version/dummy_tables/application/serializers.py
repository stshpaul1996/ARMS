from rest_framework import serializers
from . models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
 
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
 
class PurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = "__all__"
 
class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = "__all__"
 
class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrders
        fields = "__all__"
 
class PurchasesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrders
        fields = "__all__"
 
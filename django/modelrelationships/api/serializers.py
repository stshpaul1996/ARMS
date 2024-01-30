from rest_framework import serializers
from .models import Category,SalesOrder,PurchaseOrder,Product,OpeningStock,CostPrice

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=SalesOrder
        fields='__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseOrder
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class OpeningStockSerializer(serializers.ModelSerializer):
    class Meta:
        model=OpeningStock
        fields='__all__'

class CostPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model=CostPrice
        fields='__all__'
from rest_framework import serializers
from .models import Category, PurchaseOrder, SalesOrder, Product, ProductCost, OpeningStock, ProductPurchases, ProductSales, Stock

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCost
        fields = '__all__'

class OpeningStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningStock
        fields = '__all__'

class ProductPurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPurchases
        fields = '__all__'

class ProductSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSales
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

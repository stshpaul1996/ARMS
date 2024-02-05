from rest_framework import serializers
from . models import Category,Product,Sales,Purchase,OpeningStock

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    stock=serializers.DecimalField(source="openingstock.stock",max_digits=10,decimal_places=2)
    class Meta:
        model = Product
        fields = ("id","name","unique_number","cost","category","stock")

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields="__all__"

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields="__all__"

class OpeningStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningStock
        fields="__all__"


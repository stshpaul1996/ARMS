from rest_framework import serializers
from .models import *

class CategorySer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSer(serializers.ModelSerializer):
    class Meta:
        stock = serializers.DecimalField(source="openingstock.stock", max_digits=10, decimal_places=2)
        model = Product
        fields = ("id", "name", "unique_num", "category", "cost")

class SalesSer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = "__all__"

class PurchaseSer(serializers.ModelSerializer):
    class Meta:
        #stock = serializers.DecimalField(source="openingstock.stock", max_digits=10, decimal_places=2)
        model = Purchase
        fields = "__all__"

        # ("name", "unqiue_num", "category",
        #           "cost", "stock")

class OpeningStockSer(serializers.ModelSerializer):
    class Meta:
        models = OpeningStock
        fields = "__all__"
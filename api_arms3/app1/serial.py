from rest_framework import serializers
from .models import *

class Categorys(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'

class Products(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'

class saless(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class Purchases(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class OpeningStocks(serializers.ModelSerializer):
    class Meta:
        model = OpeningStock
        fields = '__all__'

class Stocks(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields ='__all__'
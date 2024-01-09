from rest_framework import serializers
from app1.models import Product, OpeningStock, Selling, Purchasing, Stock

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OpeningStockserializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningStock
        fields = '__all__'

class Sellingserializer(serializers.ModelSerializer):
    class Meta:
        model = Selling
        fields = '__all__'

class Purchasingserializer(serializers.ModelSerializer):
    class Meta:
        model = Purchasing
        fields = '__all__'

class Stockserializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
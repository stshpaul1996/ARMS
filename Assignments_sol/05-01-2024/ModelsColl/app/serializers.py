from rest_framework import serializers
from .models import *

class productdata(serializers.Serializer):
    productname = serializers.CharField(max_length=50)
    openingstock = serializers.DecimalField(max_digits=10, decimal_places=2)
    product_unique_number = serializers.IntegerField()
    Cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    date = serializers.DateField()
    catogory = serializers.CharField(max_length=50)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = '__all__'

# class ProductSerializer(serializers.ModelSerializer):
#     catogory = serializers.CharField(source = 'Category.catogory')
#     cost = serializers.CharField(source = 'Cost.Cost')
#     date =serializers.DateField(source='Cost.date')
#     class Meta:
#         model = Product
#         fields = ("catogory","cost",'date','productname','openingstock','product_unique_number')

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.category')
    cost = serializers.DecimalField(source='cost.cost', max_digits=10, decimal_places=2)
    date = serializers.DateField(source='cost.date')

    class Meta:
        model = Product
        fields = ("category", "cost", 'date', 'productname', 'openingstock', 'product_unique_number')

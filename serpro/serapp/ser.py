from rest_framework import serializers


from .models import *

class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CostSer(serializers.ModelSerializer):
    class Meta:
        model = ProductCost
        fields = "__all__"

class CategorySer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

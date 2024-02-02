from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class RoleSerializer(serializers.ModelSerializer):
     class Meta:
        model = Role
        fields = ["name"]


class UserSerializer(serializers.ModelSerializer):
    role = serializers.IntegerField()

    class Meta:
        model = User
        fields = ["username", "password","email", "role"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class OpeningStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningStock
        fields = "__all__"

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = "__all__"

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"
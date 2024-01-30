from rest_framework import serializers
from .models import Category,SalesOrder,PurchaseOrder,Product,OpeningStock,CostPrice,Stock,PPOS,SSOS,FinalStockReport

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

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Product
#         fields='__all__'
        
class ProductSerializer(serializers.ModelSerializer):
 
    cost = serializers.SerializerMethodField()
    stock = serializers.SerializerMethodField()
    purchasestock=serializers.SerializerMethodField()
    salestock=serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ("id","name", "product_unique_number", "category", "cost", "stock",'purchasestock','salestock')
 
    def get_cost(self, obj):
        productcost = obj.product_costs.first()
        return productcost.cost if productcost else None
 
    def get_stock(self, obj):
        openingstock = obj.product_stock.first()
        return openingstock.stock if openingstock else None
    
    def get_purchasestock(self, obj):
        purchasestock = obj.purchase_stock.first()
        return purchasestock.purchasestock if purchasestock else None
    
    def get_salestock(self, obj):
        salestock = obj.purchase_stock.first()
        return salestock.salestock if salestock else None
    
class OpeningStockSerializer(serializers.ModelSerializer):
    class Meta:
        model=OpeningStock
        fields='__all__'

class CostPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model=CostPrice
        fields='__all__'

class PPOSSerializer(serializers.ModelSerializer):
    class Meta:
        model=PPOS
        fields='__all__'

class SSOSSerializer(serializers.ModelSerializer):
    class Meta:
        model=SSOS
        fields='__all__'

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'

class FinalStockReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=FinalStockReport
        fields='__all__'
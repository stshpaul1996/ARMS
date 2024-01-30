from rest_framework import serializers
from .models import product,category,PurchaseOrder,SalesOrder,stock,productcost,ppos,ssos,StockReport




class PurchaseSerializer(serializers.ModelSerializer):
    class Meta :
        model = PurchaseOrder
        fields = "__all__"





class ProductSerializer(serializers.ModelSerializer):

    cost = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()
 
    class Meta:
        model = product
        fields = ("name", "product_unq_number", "category_id", "cost", "quantity")
 
    def get_cost(self, obj):
        productcost = obj.productcost_set.first()
        return productcost.cost if productcost else None
 
    def get_quantity(self, obj):
        openingstock = obj.stock_set.first()
        return openingstock.quantity if openingstock else None





    
    # cost = serializers.DecimalField(source = 'productcost.cost' ,max_digits=10,decimal_places=2)
    # quantity = serializers.DecimalField(source= 'stock.quantity' ,max_digits=10,decimal_places=2)
    
    # class Meta:
    #     model = product
    #     fields = ('name','product_unq_number',"category_id",'cost','quantity')


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = stock
        fields = "__all__"




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = "__all__"


class PposSertializer(serializers.ModelSerializer):
    class Meta:
        model  = ppos
        fields = "__all__"


from rest_framework import serializers

class StockReportSerializer(serializers.Serializer):
    product_id_id = serializers.IntegerField()
    name = serializers.CharField()
    product_unq_number = serializers.CharField()
    category_name = serializers.CharField()
    num_of_quantity_purchase = serializers.DecimalField(max_digits=10, decimal_places=2)
    opening_stock = serializers.DecimalField(max_digits=10, decimal_places=2)
    num_of_quantity_sale = serializers.DecimalField(max_digits=10, decimal_places=2)
    quantity_onhand = serializers.DecimalField(max_digits=10, decimal_places=2)
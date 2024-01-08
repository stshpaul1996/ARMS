from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from erpApp.models import *
from erpApp.serializers import *
from rest_framework import status
from django.db.models import Sum
import datetime

# Create your views here.


class CategoryView(APIView):
    def post(self,request):
        ser = CategorySerializer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response("Data Added Successfully")
        else:
            return Response(ser.errors)
class ProductView(APIView):
    def post(self,request):
        ser = ProductSerializer(data = request.data)
        if ser.is_valid():
            product = ser.save()
            # stock_data = request.data.get("stock")
            # opening_stock = OpeningStock(stock=stock_data,product=product)
            # opening_stock.save()
            # stock = Stock(stock = stock_data,product = product)
            # stock.save()
            return Response("Data Added Successfully")
        else:
            return Response(ser.errors)
        
class OpeningStockView(APIView):
    def post(self,request):
        ser = OpeningStockSerializer(data = request.data)
        if ser.is_valid():
            opening_stock = ser.save()
            Stock.objects.create(product = opening_stock.product,description = "Opnening stock added",refid = opening_stock.id,type = "opening",stock = opening_stock.stock)
            return Response("Data Added Successfully")
        else:
            return Response(ser.errors)
class ProductSalesView(APIView):
    def post(self,request):
        ser = ProductSalesSerializer(data = request.data)
        if ser.is_valid():
            sales = ser.save()
            Stock.objects.create(product = sales.product,description = "Opnening stock added",refid = sales.id,type = "sales",stock = -(sales.stock))
            return Response("Data Added Successfully")
        else:
            return Response(ser.errors)
class ProductPurchaseView(APIView):
    def post(self,request):
        ser = ProductPurchaseSerializer(data = request.data)
        if ser.is_valid():
            purchases = ser.save()
            purchases = ProductPurchaseSerializer(product = purchases.product,description = "Opnening stock added",refid = purchases.id,type = "sales",stock = purchases.stock)
            if purchases.is_valid():
                purchases.save()
            return Response("Data Added Successfully")
        else:
            return Response(ser.errors)
        
class StockView(APIView):
    def get(self,request,id):
        data  = Stock.objects.filter(product__id=id).aggregate(total_quantity=Sum('stock5 '))
        return Response({"data":data})
        
        

               
    

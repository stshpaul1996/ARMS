from django.shortcuts import render
from . models import Category,Product,Sales,Purchase,OpeningStock
from . serializers import CategorySerializer,ProductSerializer,SalesSerializer,PurchaseSerializer,OpeningStockSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CategoryView(APIView):
    def get(self, request,pk=None, *args, **kwargs):
        if pk:
            category=Category.objects.get(pk=pk)
            serializer=CategorySerializer(category)
        else:
            category=Category.objects.all()
            serializer=CategorySerializer(category,many=True)
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Inserted data successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.error,status_code=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        catagory=Category.objects.get(pk=pk)
        serializer=CategorySerializer(catagory,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request,pk):
        category=Category.objects.get(pk=pk)
        serializer=CategorySerializer(category,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        category=Category.objects.get(pk=pk)
        category.delete()
        return Response({"msg":"data deleted successfully"},status=status.HTTP_204_NO_CONTENT)
    
class ProductView(APIView):
    def get(self, request,pk=None, *args, **kwargs):
        if pk:
            product=Product.objects.get(pk=pk)
            serializer=ProductSerializer(product)
        else:
            product=Product.objects.all()
            serializer=ProductSerializer(product,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            sa=serializer.save()
            sa.openingstock_set.create(stock=request.data.get("stock"))
            return Response({"data":request.data,"msg":"Inserted data successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.error,status_code=status.HTTP_400_BAD_REQUEST)
    
class PurchaseView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":request.data,"msg":"Inserted data successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.error,status_code=status.HTTP_400_BAD_REQUEST)

class SalesView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=SalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":request.data,"msg":"Inserted data successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.error,status_code=status.HTTP_400_BAD_REQUEST)
    
class StockView(APIView):
    def get(self, request, *args, **kwargs):
        pro=Product.objects.get(id=1)
        purchase=Purchase.objects.get(product=pro.id)
        sales=Sales.objects.get(product=pro.id)
        o=OpeningStock.objects.get(id=1)
        rem_stock=o.stock+purchase.stock-sales.stock
        return Response({"rem_stock":rem_stock})

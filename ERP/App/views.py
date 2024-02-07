from django.shortcuts import render

from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from django.db.models import Sum
from .serializers import *
# Create your views here.

class CategoryView(APIView):
    def post(self,request):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data},status = status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def get(self,request,id = None):
        if id == None:
            instance = Category.objects.all()
            serializer  = CategorySerializer(instance,many=True)
            return Response(serializer.data)
        else:
            instance = Category.objects.get(id = id)
            serializer  = CategorySerializer(instance)
            return Response(serializer.data)
        
class ProductView(APIView):
    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
           data = serializer.save()
        
           
           OpeningStock.objects.create(product = data,stock = data.opening_stock)
           return Response("data added successfully",status= status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def get(self,request,id = None):
        if id ==None:
            instance = Product.objects.all()
            serializer = ProductSerializer(instance,many = True)
            return Response(serializer.data)
        else:
            instance = Product.objects.get(id = id)
            serializer = ProductSerializer(instance)
            return Response(serializer.data)
        
class SalesView(APIView):
    def post(self,request):
        lst = []
        for i in request.data:
            
            serializer = SalesSerializer(data = i)
            if serializer.is_valid():
                serializer.save()
                
                lst.append(serializer.data)
            else:
                return Response(serializer.errors)
        return Response({"data":lst})
    
    def get(self,request,id = None):
        if id == None:
            instance = Sales.objects.all()
            serializer = SalesSerializer(instance,many = True)

            return Response(serializer.data)
        else:
            instance = Sales.objects.get(id = id)
            serializer = SalesSerializer(instance)
            return Response(serializer.data)

class PurchaseView(APIView):
    def post(self,request):
        lst = []
        for i in request.data:
            
            serializer = PurchaseSerializer(data = i)
            if serializer.is_valid():
                serializer.save()
                
                lst.append(serializer.data)
            else:
                return Response(serializer.errors)
        return Response({"data":lst})
    
    def get(self,request,id = None):
        if id == None:
            instance = Sales.objects.all()
            serializer = PurchaseSerializer(instance,many = True)

            return Response(serializer.data)
        else:
            instance = Sales.objects.get(id = id)
            serializer = PurchaseSerializer(instance)
            return Response(serializer.data)

class StockReportView(APIView):
    def get(self, request, id, *args, **kwargs):
        product = Product.objects.get(id=id)
        opening_stock = OpeningStock.objects.filter(product_id=id).aggregate(total_stock=Sum('stock'))['total_stock'] or 0
        total_purchase_stock = Purchase.objects.filter(product_id=id).aggregate(total_stock=Sum('quantity_p'))['total_stock'] or 0
        total_sale_stock = Sales.objects.filter(product_id=id).aggregate(total_stock=Sum('quantity_s'))['total_stock'] or 0
        category_serializer = CategorySerializer(product.category)
        response_data = {
            'product_id': product.id,
            'product_name': product.name,
            'product_category': category_serializer.data,
            'product_unique_num': product.product_unique_number,
            'opening_stock': opening_stock,
            'no_of_quantity_purchase': total_purchase_stock,
            'no_of_quantity_sale': total_sale_stock,
            'quantity_onhand': (opening_stock + total_purchase_stock - total_sale_stock)
        }
 
        return Response(response_data, status=status.HTTP_200_OK)
 
 
class StockReportAllView(APIView):
    def get(self, request, *args, **kwargs):
        # Get all products
        products = Product.objects.all()
        # Initialize an empty list to store response data for each product
        response_data_list = []
        # Iterate over each product and retrieve the required information
        for product in products:
            opening_stock = OpeningStock.objects.filter(product_id=product.id).aggregate(total_stock=Sum('stock'))['total_stock']
            total_purchase_stock = Purchase.objects.filter(product_id=product.id).aggregate(total_stock=Sum('quantity_p'))['total_stock']
            total_sale_stock = Sales.objects.filter(product_id=product.id).aggregate(total_stock=Sum('quantity_s'))['total_stock']
            category_serializer = CategorySerializer(product.category)
           
            # Create response data for each product
            product_data = {
                'product_id': product.id,
                'product_name': product.name,
                'product_category': category_serializer.data,
                'product_unique_num': product.product_unique_number,
                'opening_stock': opening_stock,
                'no_of_quantity_purchase': total_purchase_stock,
                'no_of_quantity_sale': total_sale_stock,
                'quantity_onhand': (opening_stock + total_purchase_stock - total_sale_stock)
            }
 
            # Append the product data to the response data list
            response_data_list.append(product_data)
 
        # Return the response data list
        return Response(response_data_list, status=status.HTTP_200_OK)
 
 
 
 
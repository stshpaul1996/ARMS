from django.shortcuts import render
from app1.models import Product, OpeningStock, Selling, Purchasing, Stock
from app1.serializer import Productserializer, Sellingserializer, OpeningStockserializer, Stockserializer, Purchasingserializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class ProductV(APIView):
    def post(self, request):
        message = ''
        p = Productserializer(data=request.data)
        if p.is_valid():
            p.save()
            message = 'Data is inserted'
        else:
            message = 'Data is not inserted'
        return Response(message)
class OpeningStockV(APIView):
    def post(self, request):
        message = ''
        opening_stock_serializer = OpeningStockserializer(data=request.data)
        
        if opening_stock_serializer.is_valid():
            opening_stock_serializer.save()
            0
            # Now, update or create a Stock record for the same product
            product_instance = opening_stock_serializer.validated_data['name']
            stock_data = {
                'name': product_instance,
                'type': 'OP', 
                'units': opening_stock_serializer.validated_data['units'],
            }
            
            stock_serializer = Stockserializer(data=stock_data)
            
            if stock_serializer.is_valid():
                stock_serializer.save()
                message = 'Opening Stock and Stock data inserted successfully.'
            else:
                message = 'Opening Stock inserted, but Stock data not inserted.'
        else:
            message = 'Data is not inserted'
        
        return Response(message, status=status.HTTP_201_CREATED)
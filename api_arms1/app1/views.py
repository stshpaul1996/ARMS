from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import *
from app1.serializers import (ProductModelSerializer,
                              CategoryModelSerializer)
from rest_framework import status

# Create your views here.

class CategoryView(APIView):
    def post(self, request):
        data = {}
        ser = CategoryModelSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            message = "inserted successfully"
            status_code = status.HTTP_201_CREATED
            data = ser.data
        else:
            message=ser.errors
            status_code = status.HTTP_400_BAD_REQUEST

        return Response({"Result":message,"data": data}, status=status_code)

class ProductView(APIView):
    def post(self, request):
        data = {}
        ser = ProductModelSerializer(data=request.data)
    
        if ser.is_valid():
            message = "inserted successfully"
            status_code = status.HTTP_201_CREATED
            data = ser.data
        else:
            message=ser.errors
            status_code = status.HTTP_400_BAD_REQUEST

        return Response({"Result":message,"data": data}, status=status_code)


    def get(self,request):
        products=Product.objects.all()
        ser=ProductModelSerializer(products,many=True)
        data=ser.data 
        return Response(data)



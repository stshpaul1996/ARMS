from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category,SalesOrder,PurchaseOrder,Product,OpeningStock,CostPrice
from .serializers import CategorySerializer,SalesOrderSerializer,PurchaseOrderSerializer,ProductSerializer,OpeningStockSerializer,CostPriceSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class CategoryView(APIView):
    def get(self,request,pk=None):
        id = pk
        if id is not None:
            cat = Category.objects.get(id=id)
            ser = CategorySerializer(cat)
            return Response(ser.data)
        cat=Category.objects.all()
        ser=CategorySerializer(cat,many=True)
        return Response(ser.data)
    
    def post(self,request):
        ser=CategorySerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            status_code=status.HTTP_201_CREATED
            return Response({'msg':'Inserted data successfully'},status=status_code)
        return Response(ser.error,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        id=pk
        cat=Category.objects.get(pk=id)
        ser=CategorySerializer(cat,data=request.data)
        if ser.is_valid():
            status_code=status.HTTP_201_CREATED
            return Response({'msg':'completely updated'},status=status_code)
        return Response(ser.data,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        id=pk
        cat=Category.objects.get(pk=id)
        ser=CategorySerializer(cat,data=request.data,partial=True)
        if ser.is_valid():
            status_code=status.HTTP_201_CREATED
            return Response({'msg':'partially updated'},status=status_code)
        return Response(ser.data,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        id=pk
        cat=Category.objects.get(pk=id)
        cat.delete()
        return Response({'msg':'DATA DELETED SUCCESSFULLY'})
    
class SalesOrderView(APIView):
    def get(self,request,pk=None):
        id = pk
        if id is not None:
            sales = SalesOrder.objects.get(id=id)
            ser = SalesOrderSerializer(sales)
            return Response(ser.data)
        sales=SalesOrder.objects.all()
        ser=SalesOrderSerializer(sales,many=True)
        return Response(ser.data)
    
    def post(self,request):
        ser=SalesOrderSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            status_code=status.HTTP_201_CREATED
            return Response({'msg':'Inserted data successfully'},status=status_code)
        return Response(ser.error,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        id=pk
        sales=SalesOrder.objects.get(pk=id)
        ser=SalesOrderSerializer(sales,data=request.data)
        if ser.is_valid():
            status_code=status.HTTP_201_CREATED
            return Response({'msg':'completely updated'},status=status_code)
        return Response(ser.data,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        id=pk
        sales=SalesOrder.objects.get(pk=id)
        ser=SalesOrderSerializer(sales,data=request.data,partial=True)
        if ser.is_valid():
            status_code=status.HTTP_201_CREATED
            return Response({'msg':'partially updated'},status=status_code)
        return Response(ser.data,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        id=pk
        sales=SalesOrder.objects.get(pk=id)
        sales.delete()
        return Response({'msg':'DATA DELETED SUCCESSFULLY'})
    
class PurchaseOrderView(APIView):
    def get(self,request,pk=None):
        id = pk
        if id is not None:
            Purchase = PurchaseOrder.objects.get(id=id)
            ser = ProductSerializer(Purchase)
            return Response(ser.data)
        Purchase=Product.objects.all()
        ser=PurchaseOrderSerializer(Purchase,many=True)
        return Response(ser.data)
    
    def post(self,request):
        ser=PurchaseOrderSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            status_code=status.HTTP_201_CREATED
            return Response({'msg':'Inserted data successfully'},status=status_code)
        return Response(ser.error,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        id=pk
        Purchase=PurchaseOrder.objects.get(pk=id)
        ser=PurchaseOrderSerializer(Purchase,data=request.data)
        if ser.is_valid():
            status_code=status.HTTP_201_CREATED
            return Response({'msg':'completely updated'},status=status_code)
        return Response(ser.data,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        id=pk
        Purchase=PurchaseOrder.objects.get(pk=id)
        ser=PurchaseOrderSerializer(Purchase,data=request.data,partial=True)
        if ser.is_valid():
            status_code=status.HTTP_201_CREATED
            return Response({'msg':'partially updated'},status=status_code)
        return Response(ser.data,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        id=pk
        Purchase=PurchaseOrder.objects.get(pk=id)
        Purchase.delete()
        return Response({'msg':'DATA DELETED SUCCESSFULLY'})
    
class ProductView(APIView):
    #import pdb;pdb.set_trace()
    def get(self,request,pk=None):
        id = pk
        if id is not None:
            Products = Product.objects.get(id=id)
            ser = ProductSerializer(Products)
            return Response(ser.data)
        Products=Product.objects.all()
        ser=ProductSerializer(Products,many=True)
        return Response(ser.data)
    
    # def post(self,request):
    #     #import pdb;pdb.set_trace()
    #     ser=ProductSerializer(data=request.data)
    #     if ser.is_valid():
    #         ser.save()
    #         status_code=status.HTTP_201_CREATED
    #         return Response({'msg':'Inserted data successfully'},status=status_code)
    #     return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            # Extract data from the request
            product_data = request.data.get('product', {})
            opening_stock_data = request.data.get('opening_stock', {})
            cost_price_data = request.data.get('cost_price', {})

            # Serialize and save Product
            product_serializer = ProductSerializer(data=product_data)
            if product_serializer.is_valid():
                product_instance = product_serializer.save()
            else:
                return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Serialize and save OpeningStock with the associated Product
            opening_stock_serializer = OpeningStockSerializer(data={**opening_stock_data, 'product': product_instance.id})
            if opening_stock_serializer.is_valid():
                opening_stock_instance = opening_stock_serializer.save()
            else:
                return Response(opening_stock_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Serialize and save CostPrice with the associated Product
            cost_price_serializer = CostPriceSerializer(data={**cost_price_data, 'product_id': product_instance.id})
            if cost_price_serializer.is_valid():
                cost_price_instance = cost_price_serializer.save()
            else:
                return Response(cost_price_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'msg': 'Inserted data successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self,request,pk):
        id=pk
        Products=Product.objects.get(pk=id)
        ser=ProductSerializer(Products,data=request.data)
        if ser.is_valid():
            status_code=status.HTTP_201_CREATED
            return Response({'msg':'completely updated'},status=status_code)
        return Response(ser.data,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        id=pk
        Products=Product.objects.get(pk=id)
        ser=ProductSerializer(Products,data=request.data,partial=True)
        if ser.is_valid():
            status_code=status.HTTP_201_CREATED
            return Response({'msg':'partially updated'},status=status_code)
        return Response(ser.data,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        id=pk
        Products=Product.objects.get(pk=id)
        Products.delete()
        return Response({'msg':'DATA DELETED SUCCESSFULLY'})
    
class OpeningStockView(APIView):
    def get(self,request,pk=None):
        id = pk
        if id is not None:
            stock = OpeningStock.objects.get(id=id)
            ser = OpeningStockSerializer(stock)
            return Response(ser.data)
        stock=OpeningStock.objects.all()
        ser=OpeningStockSerializer(stock,many=True)
        return Response(ser.data)
    
    def post(self,request):
        ser=OpeningStockSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            status_code=status.HTTP_201_CREATED
            return Response({'msg':'Inserted data successfully'},status=status_code)
        return Response(ser.error,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        id=pk
        stock=OpeningStock.objects.get(pk=id)
        ser=OpeningStockSerializer(stock,data=request.data)
        if ser.is_valid():
            status_code=status.HTTP_201_CREATED
            return Response({'msg':'completely updated'},status=status_code)
        return Response(ser.data,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        id=pk
        stock=OpeningStock.objects.get(pk=id)
        ser=OpeningStockSerializer(stock,data=request.data,partial=True)
        if ser.is_valid():
            status_code=status.HTTP_201_CREATED
            return Response({'msg':'partially updated'},status=status_code)
        return Response(ser.data,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        id=pk
        stock=OpeningStock.objects.get(pk=id)
        stock.delete()
        return Response({'msg':'DATA DELETED SUCCESSFULLY'})
    

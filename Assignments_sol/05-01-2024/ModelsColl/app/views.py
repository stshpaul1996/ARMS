from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Cost, Category
from .serializers import *

class ProductDataAPIView(APIView):
    def post(self, request):
        serializer = productdata(data=request.data)

        if serializer.is_valid():
            productname = serializer.validated_data['productname']
            openingstock = serializer.validated_data['openingstock']
            product_unique_number = serializer.validated_data['product_unique_number']
            cost = serializer.validated_data['Cost']
            date = serializer.validated_data['date']
            category_name = serializer.validated_data['catogory']

            Category.objects.get_or_create(catogory=category_name)
            Product.objects.create(
                productname=productname,
                openingstock=openingstock,
                product_unique_number=product_unique_number
            )
            Cost.objects.create(
                Cost=cost,
                date=date
            )

            return Response("Data saved successfully", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProductDataCreateAPIView(APIView):
#     def post(self, request):
#         product_serializer = ProductSerializer(data=request.data)
#         category_serializer = CategorySerializer(data=request.data.get('catogory'))
#         cost_serializer = CostSerializer(data=request.data.get('cost'))
#
#         if all([product_serializer.is_valid(), category_serializer.is_valid(), cost_serializer.is_valid()]):
#             category_serializer.save()
#             cost_serializer.save()
#             product_serializer.save()
#             return Response("Data saved successfully", status=status.HTTP_201_CREATED)
#         else :
#             errors = {
#                 'product_errors': product_serializer.errors,
#                 'category_errors': category_serializer.errors,
#                 'cost_errors': cost_serializer.errors
#             }
#             return Response(errors, status=status.HTTP_400_BAD_REQUEST)
#
# class ProductDataCreateAPIView(APIView):
#     def post(self, request):
#         product_serializer = ProductSerializer(data=request.data)
#         category_data = request.data.get('catogory')
#         cost_data = request.data.get('cost')
#
#         if product_serializer.is_valid():
#             # Save category
#             if category_data:
#                 category_serializer = CategorySerializer(data=category_data)
#                 if category_serializer.is_valid():
#                     category_instance = category_serializer.save()
#                     # Assign category instance to product serializer data
#                     product_serializer.validated_data['catogory'] = category_instance
#
#             # Save cost
#             if cost_data:
#                 cost_serializer = CostSerializer(data=cost_data)
#                 if cost_serializer.is_valid():
#                     cost_instance = cost_serializer.save()
#                     # Assign cost instance to product serializer data
#                     product_serializer.validated_data['cost'] = cost_instance
#
#             # Save the product with related data
#             product_instance = product_serializer.save()
#
#             return Response("Data saved successfully", status=status.HTTP_201_CREATED)
#         else:
#             errors = {
#                 'product_errors': product_serializer.errors,
#                 'category_errors': CategorySerializer.errors if 'category_serializer' in locals() else None,
#                 'cost_errors': CostSerializer.errors if 'cost_serializer' in locals() else None
#             }
#             return Response(errors, status=status.HTTP_400_BAD_REQUEST)

class DataCreateView(APIView):
    def post(self, request,):
        category_data = request.data.get('catogory')
        product_data = request.data.get('productname')
        opening_stock_data = request.data.get('openingstock')
        product_unique_number_data = request.data.get('product_unique_number')
        cost_data = request.data.get('Cost')
        date_data = request.data.get('date')


        category_serializer = CategorySerializer(data={'catogory': category_data})
        cost_serializer = CostSerializer(data={'Cost': cost_data, 'date': date_data})

        if category_serializer.is_valid() and cost_serializer.is_valid():
            category_serializer.save()
            cost_serializer.save()

            product_instance = Product.objects.create(
                productname=product_data,
                openingstock=opening_stock_data,
                product_unique_number=product_unique_number_data,

            )
            product_serializer = ProductSerializer(product_instance)
            return Response(product_serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
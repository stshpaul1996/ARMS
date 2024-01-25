from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serial import *
from .models import *
from django.db.models import Sum, ExpressionWrapper, IntegerField, F
from django.http import JsonResponse
# Create your views here.
class CategoryV(APIView):
    def post(self, request):
        cat = Categorys(data= request.data)
        Message = ''
        if cat.is_valid():
            cat.save()
            Message ='Data is inserted'
        else:
            Message = 'Data is not inserted'
        return Response({'Message': Message}, status=status.HTTP_201_CREATED)
    
class Productv(APIView):
    def post(self, request):
        cat_name = request.data.get('category')
        cat_p = Category.objects.get(name =cat_name) 
        pro_ins = request.data.copy()
        pro_ins['category'] = cat_p.id
        pro = Products(data=pro_ins)
        Message = ''
        if pro.is_valid():
            pro.save()
            Message = 'Data is inserted'
        else:
            Message = 'Data is not inserted'
        return Response(Message,status=status.HTTP_201_CREATED)

            
class OpeningStockV(APIView):
    def post(self, request):
        pro_name = request.data.get('product')
        pro_pro = Product.objects.get(name = pro_name)
        # pro_pro_name = pro_pro.id
        # pro_pro_uniq = pro_pro.unique_num
        # pro_id = Product.objects.get(id = pro_pro_name)
        # pro_uniq = Product.objects.get(unique_num = pro_pro_uniq)
        op = request.data.copy()
        op['product'] = pro_pro.id
        opstock = op['stock']
        op_sto = OpeningStocks(data=op)
        if op_sto.is_valid():
            op_sto.save()
        stock_data = {
                'category': pro_pro.category.id,
                'product': pro_pro.id,
                'openingStock': opstock,
                'unique_nums': pro_pro.unique_num  # Use the unique_num directly
            }
        stoc = Stocks(data=stock_data)
        if stoc.is_valid():
            stoc.save()
            Message ='Data is inserted'
        else:
            Message = 'Data is not inserted'
        return Response(Message,status=status.HTTP_201_CREATED)
    
class Salesv(APIView):
    def post(self, request):
        pro_name = request.data.get('product')
        pro_og_name = Product.objects.get(name = pro_name)
        pro_id = pro_og_name.id
        sale = request.data.copy()
        sale['product'] = pro_id
        salev = sale['stock']
        sale_inst =saless(data=sale)
        if sale_inst.is_valid():
            sale_inst.save()
        sale_data = {
                'category': pro_og_name.category.id,
                'product': pro_og_name.id,
                'unique_nums': pro_og_name.unique_num,
                'sales': salev 
            }
        stock_sale = Stocks(data= sale_data)
        if stock_sale.is_valid():
            stock_sale.save()
            Message ='Data is inserted'
        else:
            Message = 'Data is not inserted'
        return Response(Message,status=status.HTTP_201_CREATED)

class Purchasev(APIView):
    def post(self, request):
        pro_name = request.data.get('product')
        pro_id = Product.objects.get(name = pro_name)
        purc = request.data.copy()
        purc['product'] = pro_id.id
        pursto = purc['stock']
        pur_inst = Purchases(data=purc)
        if pur_inst.is_valid():
            pur_inst.save()
            mess = 'data is inserted '
        Purchase_data = {
                'category': pro_id.category.id,
                'product': pro_id.id,
                'unique_nums': pro_id.unique_num,
                'purchase': pursto
            }
        stock_inst = Stocks(data= Purchase_data)
        if stock_inst.is_valid():
            stock_inst.save()
            Message = 'Data is inserted'
        else:
            Message = 'Data is not inserted'
        return Response({'mess1':mess, 'mess2':Message},status=status.HTTP_201_CREATED)
    
class Stockv(APIView):
    def get(self, request):
        aggregated_stocks = Stock.objects.values(
            'product__name', 
            # 'product__id', 
            'unique_nums', 
            'category__name', 
            # 'category__id'
        ).annotate(
            total_opening_stock=Sum('openingStock'),
            total_sales=Sum('sales'),
            total_purchase=Sum('purchase'),
            stock_difference=ExpressionWrapper(
                F('total_purchase') - F('total_sales'), 
                output_field=IntegerField()
                )
        )
        return Response(aggregated_stocks)
# class Stockvp(APIView):
#     def get(self, request, id):
#         stvp = Stock.objects.get(product = id)
#         productid = stvp.id
#         productcat = stvp.category
#         productopen = stvp.openingStock
#         productsale = stvp.sales
#         productuniq = stvp.unique_nums

#         return Response({productid, productcat, productopen, productsale, productuniq})

class Stockvp(APIView):
    def get(self, request, id):
        stocks = Stock.objects.filter(product=id)
        results = []
        for stvp in stocks:
            results.append({
                'id': stvp.id,
                'category': stvp.category,
                'openingStock': stvp.openingStock,
                'sales': stvp.sales,
                'unique_nums': stvp.unique_nums
            })
        return JsonResponse(results, safe=False)

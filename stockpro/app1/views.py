from django.shortcuts import render
from .models import *
from .ser import *
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class CategoryView(APIView):
    def post(self, request):
        req = CategorySer(data=request.data)
        msg = ""
        if req.is_valid():
            req.save()
            msg = "success"
        else:
            msg = req.errors
        return Response({"result":msg, "data":request.data})

class ProductView(APIView):
    def post(self,request):
        req = ProductSer(data=request.data)
        msg = ""
        #import pdb;pdb.set_trace()
        data={}
        if req.is_valid():
            sa = req.save()
            #import pdb;pdb.set_trace()
            # data = req.data
            # data.update({"id":sa.id})

            sa.openingstock_set.create(stock=request.data.get("stock"))
            msg="success"
        else:
            msg=req.errors
        return Response({"result":msg,"data":request.data})

class PurchaseView(APIView):
    def post(self, request):
        req = PurchaseSer(data=request.data)
        msg = ""
        if req.is_valid():
            req.save()
            msg = "success"
        else:
            msg = req.errors
        return Response({"result":msg, "data":request.data})


class SaleView(APIView):
    def post(self, request):
        req = SalesSer(data=request.data)
        msg=""
        if req.is_valid():
            req.save()
            msg="success"
        else:
            msg = req.errors

        return Response({"result":msg, "data":request.data})



class StockView(APIView):
    def get(self, request):
        pro = Product.objects.get(id=1)
        pro_ser = ProductSer(pro, many=True)
        purchase = Purchase.objects.get(id=pro.id)
        sales = Sales.objects.get(id=pro.id)
        o = OpeningStock.objects.get(id=1)
        rem_stock = purchase.stock-sales.stock+o.stock
        # print(purchase.stock)
        # print(sales.stock)
        # print(pro.id)
        return Response({"rem_stock":rem_stock})

        
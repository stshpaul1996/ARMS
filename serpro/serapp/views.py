from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .ser import ProductSer, CostSer, CategorySer
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from datetime import datetime

class ProductView(APIView):
    def post(self, request):
        req = ProductSer(data=request.data)
        msg = ""
        if req.is_valid():
            req.save()
            msg = "success"
        else:
            msg = req.errors
        
        return Response({"result":msg, "data_inserted": req.data})
    
    def patch(self, request,id):
        db_data = Product.objects.get(id=id)
        req = ProductSer(db_data, data=request.data, partial=True)
        msg = ""
        if req.is_valid():
            req.save()
            
            pro_id= Product.objects.get(pk=id)
            
            cost = ProductCost(cost=request.data.get("cost"), created=datetime.now(), product=pro_id)
            cost.save()
            msg = "success"
        else:
            msg = req.errors
        
        return Response({"res":msg, "data":req.data})


class CategoryView(APIView):
    def post(self, request):
        req = CategorySer(data=request.data)
        msg = ""
        if req.is_valid():
            req.save()
            msg = "success"
        else:
            msg = req.errors
        
        return Response({"result":msg, "data_inserted":req.data})

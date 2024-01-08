from django.shortcuts import render
from django.db.models import Sum

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer,CategorySerializer,StockSerializer,PposSertializer

from .models import product,category,PurchaseOrder,SalesOrder,stock,StockReport,ppos,ssos



class Purchase(APIView):
    def post(self,request):
        data = request.data 
        
        product_instance = product.objects.get(pk=data.get("product_id"))
        purchase_inst = PurchaseOrder(description=data.get("description"))
        purchase_inst.save()

        product_purchase_inst = ppos( product_id= product_instance,purchase_id=purchase_inst,quantity=data.get('quantity'))
        product_purchase_inst.save()

        

        stock_report_inst = StockReport(description=data.get("description"), product_id =product_instance, type='PS', quantity=data.get('quantity'))
        stock_report_inst.save()
        return Response("hy")

class Sale(APIView):
    def post(self,request):
        data = request.data 
        
        product_instance = product.objects.get(pk=data.get("product_id"))
        sale_inst = SalesOrder(description=data.get("description"))
        sale_inst.save()

        product_purchase_inst = ssos( product_id= product_instance,sale_id=sale_inst,quantity=data.get('quantity'))
        product_purchase_inst.save()

        stock_report_inst = StockReport(description=data.get("description"), product_id =product_instance, type='SS', quantity=-(data.get('quantity')))
        stock_report_inst.save()
        return Response("hy")

class SaleReport(APIView):
    def get(self,request,id):
        data  = StockReport.objects.filter(product_id__id=id).aggregate(total_quantity=Sum('quantity'))
        return Response({"data":data})
    


class ProductView(APIView):
    def get(self,request):
        products = product.objects.all()
        data = ProductSerializer(products,many=True)
        return Response({"data":data.data})
        
    
    def post(self,request):
        data = request.data
        
        print(data)
        
        inst = ProductSerializer(data=request.data)

       
        message = ""
        if inst.is_valid():
            

            
            ser = inst.save()
            
           
            ser.productcost_set.create(cost=request.data.get('cost'))
            ser.stock_set.create(quantity=request.data.get('quantity'))
            stock_report_inst = StockReport(description="opesningstock in added", product_id =ser, type='OS', quantity=data.get('quantity'))
            
            stock_report_inst.save()

            message = "Data added successfully"
        else :
            message = "sorry....! Data not added"
        return Response({"message":message})

    def put(self,request,**kwrdargs):

        import pdb;pdb.set_trace()


        data = request.data

        Row_instance = product.objects.get(id=kwrdargs['pk'])

        k = ProductSerializer(data=Row_instance)
        message = ""

        for i,j in data.items():
            if hasattr(k,i):
                setattr(k,i,j)

        
        if k.is_valid():
            k.save()
            message="updated"
        # except Exception as err:
        #     message = str(err)

        return Response({'msg':message})
        
        products = product.objects.all()
        return Response("This is put vies")
    def delete(self,request):
        products = product.objects.all()
        return Response("This is delete vies")
    

class CategoryView(APIView):
    def get(self,request):
        categories = category.objects.all()
        ser = CategorySerializer(categories,many=True)
        
        return Response({"data":ser.data})
    
    def post(self,request):
        data = request.data
        inst = CategorySerializer(data=request.data)
        message = ""
        if inst.is_valid():
            inst.save()
            message = "Data added successfully"
        else :
            message = "sorry....! Data not added"
        return Response({"messege":message})

    def put(self,request):
        products = product.objects.all()
        return Response("This is put vies")
    def delete(self,request):
        products = product.objects.all()
        return Response("This is delete vies")

# class ProductView(APIView):
#     def get(self,request):
#         products = product.objects.all()
#         data = ProductSerializer(products,many=True)
#         return Response({"data":data})
    
#     def post(self,request):
#         products = product.objects.all()
#         return Response("This is post vies")

#     def put(self,request):
#         products = product.objects.all()
#         return Response("This is put vies")
#     def delete(self,request):
#         products = product.objects.all()
#         return Response("This is delete vies")

# class ProductView(APIView):
#     def get(self,request):
#         products = product.objects.all()
#         data = ProductSerializer(products,many=True)
#         return Response({"data":data})
    
#     def post(self,request):
#         products = product.objects.all()
#         return Response("This is post vies")

#     def put(self,request):
#         products = product.objects.all()
#         return Response("This is put vies")
#     def delete(self,request):
#         products = product.objects.all()
#         return Response("This is delete vies")

     


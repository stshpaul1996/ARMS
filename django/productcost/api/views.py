from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category,SalesOrder,PurchaseOrder,Product,OpeningStock,PPOS,SSOS,Stock,FinalStockReport
from .serializers import CategorySerializer,SalesOrderSerializer,PurchaseOrderSerializer,ProductSerializer,FinalStockReportSerializer,OpeningStockSerializer,CostPriceSerializer,StockSerializer,PPOSSerializer,SSOSSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
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
        Purchase=PurchaseOrder.objects.all()
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

    # def post(self,request):
    #     data = request.data
    #     product_instance = Product.objects.get(pk=data.get("id"))
    #     print(product_instance)

    #     inst = ProductSerializer(data=request.data)
        
    #     message = ""
        
    #     if inst.is_valid():
    #         ser = inst.save()
    #         ser.product_costs.create(cost=request.data.get('cost'))
    #         ser.product_stock.create(stock=request.data.get('stock'))
    #         message = "Insterted successfully"
    #     else :
    #         message = "No data"
    #     return Response({"message":message})


    def post(self,request):
        data=request.data
        print(data)

        inst=ProductSerializer(data=request.data)
        print(inst.is_valid())
        print(inst.errors)
        if inst.is_valid():
            ser=inst.save()
            # import pdb;pdb.set_trace()
            # product_instance = Product(name=data.get('name'))
            # print(product_instance)
            # sale_inst = Product(name=data.get('name'))
            # print(type(sale_inst))
            # #sale_inst = SalesOrder(description=data.get("description"))
            # sale_inst.save()

            #product_purchase_inst = SSOS( product_id= product_instance,sale_id=sale_inst,stock=data.get('stock'))
            #product_purchase_inst.save()
            product_instance = Product.objects.get(pk=data.get("id"))
            
            stock_report_inst = FinalStockReport(name=data.get("name"),product_unique_number=data.get('product_unique_number'),oenping_stock=data.get('stock'),product_id=product_instance,
                                                 category_id=data.get('category'))
            stock_report_inst.save()

            
            ser.product_costs.create(cost=request.data.get('cost'))
            ser.product_stock.create(stock=request.data.get('stock'))
            ser.purchase_stock.create(purchasestock=request.data.get('purchasestock'),salestock=request.data.get('salestock'))
            
            return Response({'data':data},status=status.HTTP_201_CREATED)
        else:
            return Response(inst.errors,status=status.HTTP_400_BAD_REQUEST)

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
        data=request.data
        ser=OpeningStockSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            status_code=status.HTTP_201_CREATED
            return Response({'msg':'Inserted data successfully'},status=status_code)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
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

class Purchase(APIView):
    def get(self,request,pk=None):
        id = pk
        if id is not None:
            stock = PPOS.objects.get(id=id)
            ser = PPOSSerializer(stock)
            return Response(ser.data)
        stock=PPOS.objects.all()
        ser=PPOSSerializer(stock,many=True)
        return Response(ser.data)
    
    def post(self,request):
        data = request.data 
        
        print(data)
        product_instance = Product.objects.get(pk=data.get("product_id"))
        print(product_instance)
        purchase_inst = PurchaseOrder(description=data.get("description"))
        print(purchase_inst)
        purchase_inst.save()

        product_purchase_inst = PPOS( product_id= product_instance,purchase_id=purchase_inst,stock=data.get('stock'))
        print(product_purchase_inst)
        product_purchase_inst.save()

        

        stock_report_inst = Stock(description=data.get("description"), product =product_instance, type='PS', stock=data.get('stock'))
        print(stock_report_inst)
        stock_report_inst.save()



        return Response({"data":data})

class Sale(APIView):
    def get(self,request,pk=None):
        id = pk
        if id is not None:
            stock = SSOS.objects.get(id=id)
            ser = SSOSSerializer(stock)
            return Response(ser.data)
        stock=SSOS.objects.all()
        ser=SSOSSerializer(stock,many=True)
        return Response(ser.data)
    
    def post(self,request):
        data = request.data 
        
        product_instance = Product.objects.get(pk=data.get("product_id"))
        sale_inst = SalesOrder(description=data.get("description"))
        sale_inst.save()

        product_purchase_inst = SSOS( product_id= product_instance,sale_id=sale_inst,stock=data.get('stock'))
        product_purchase_inst.save()

        stock_report_inst = Stock(description=data.get("description"), product =product_instance, type='SS', stock=(data.get('stock')))
        stock_report_inst.save()

        final_stock=FinalStockReport(name=data.get('name'),product_id=product_instance,product_unique_number=data.get('product_unique_number'),category=data.get('category'))
        print(final_stock)
        final_stock.save
        return Response({"data":data})

class StockView(APIView):
    def get(self,request,id):
        data  = Stock.objects.filter(product_id__id=id).aggregate(total_stock=Sum('stock'))
        return Response({"data":data},status=status.HTTP_200_OK)

class FainalStockReportView(APIView):
    def get(self,request,pk=None):
        id = pk
        if id is not None:
            stock = FinalStockReport.objects.filter(product_id__id=id)
            ser = FinalStockReportSerializer(stock)
            print(ser)
            return Response(ser.data)
        stock=FinalStockReport.objects.all()
        ser=FinalStockReportSerializer(stock,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)



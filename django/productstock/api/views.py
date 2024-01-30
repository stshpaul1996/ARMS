from django.shortcuts import render
from rest_framework import views
from .models import Category,Product,OpeningStock,PPOS,SSOS,Stock
from .serializers import CategorySerializer,ProductSerializer,OpeningStockSerializer,CostPriceSerializer,StockSerializer,PPOSSerializer,SSOSSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum

# Create your views here.

class CategoryView(views.APIView):
    #authentication_classes=[TokenAuthentication]
    #permission_classes=[IsAuthenticated]
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
    
 
class ProductView(views.APIView):
    def get(self,request,pk=None):
        id = pk
        if id is not None:
            Products = Product.objects.get(id=id)
            ser = ProductSerializer(Products)
            return Response(ser.data)
        Products=Product.objects.all()
        ser=ProductSerializer(Products,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)

    def post(self,request):
        data = request.data
        print(data)
        #import pdb;pdb.set_trace()
        product_instance = Product.objects.get(id=data.get("id"))
        #print(product_instance)

        inst = ProductSerializer(data=request.data)
        message = ""
        print(inst.is_valid())
        if inst.is_valid():
            ser = inst.save()
            ser.product_costs.create(cost=request.data.get('cost'))
            ser.product_stock.create(stock=request.data.get('stock'))

            stock_report_inst = Stock(description=data.get("description"),product=product_instance, type='OS', stock=(data.get('stock')))
            stock_report_inst.save()

            message = "Insterted successfully"
            return Response({'message':message},status=status.HTTP_201_CREATED)
        else :
            message = "No data"
        return Response(ser.error,{"message":message},status=status.HTTP_400_BAD_REQUEST)


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
    
class OpeningStockView(views.APIView):
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

class Purchase(views.APIView):
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
        
        product_instance = Product.objects.get(pk=data.get("product_id"))
        print(product_instance)
        
        product_purchase_inst = PPOS( description=data.get('description'),product_id= product_instance,purchasestock=data.get('purchasestock'))
        print(product_purchase_inst)
        product_purchase_inst.save()

        stock_report_inst = Stock(description=data.get("description"), product =product_instance, type='PS', stock=data.get('purchasestock'))
        print(stock_report_inst)
        stock_report_inst.save()



        return Response({"data":data})

class Sale(views.APIView):
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

        product_purchase_inst = SSOS(description=data.get('description'), product_id= product_instance,salestock=data.get('salestock'))
        product_purchase_inst.save()

        stock_report_inst = Stock(description=data.get("description"), product =product_instance, type='SS', stock=(data.get('salestock')))
        stock_report_inst.save()

        
        return Response({"data":data})

# class StockView(APIView):
#     def get(self,request,id):
#         data  = Stock.objects.filter(product_id__id=id).aggregate(total_stock=Sum('stock'))
#         print(data)
#         for i in data:
#             print(i)
#         return Response({"data":data},status=status.HTTP_200_OK)




class StockView(views.APIView):
    def get(self, request, id):
        try:
            # Get product, purchase, and sales data using serializers
            product_data = ProductSerializer(Product.objects.get(id=id)).data
            purchase_data = PPOSSerializer(PPOS.objects.filter(product_id__id=id), many=True).data
            print(purchase_data)
            sales_data = SSOSSerializer(SSOS.objects.filter(product_id__id=id), many=True).data 

            # Get total stock
            total_stock = Stock.objects.filter(product_id__id=id).aggregate(total_stock=Sum('stock'))['total_stock']

            response_data = {
                "product_data": product_data,
                "purchase_data": purchase_data,
                "sales_data": sales_data,
                "total_stock": total_stock
            }

            return Response({"data": response_data}, status=status.HTTP_200_OK)

        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



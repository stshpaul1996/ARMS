from django.shortcuts import render
from django.db.models import Sum,Q


# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer,CategorySerializer,StockSerializer,PposSertializer,StockReportSerializer

from .models import product,category,PurchaseOrder,SalesOrder,stock,StockReport,ppos,ssos



from django.db import connection


def single_object(id):

    with connection.cursor() as cursor:
        
        sql_query = """
            SELECT sr.product_id_id,
                   p.name AS product_name,
                   p.product_unq_number,
                   c.name AS category_name,
                   SUM(CASE WHEN sr.type = 'PS' THEN sr.quantity ELSE 0 END) AS num_of_quantity_purchase,
                   SUM(CASE WHEN sr.type = 'OS' THEN sr.quantity ELSE 0 END) AS opening_stock,
                   SUM(CASE WHEN sr.type = 'SS' THEN sr.quantity ELSE 0 END) AS num_of_quantity_sale,
                   SUM(sr.quantity) AS quantity_onhand
            FROM testapp_stockreport sr
            JOIN testapp_product p ON sr.product_id_id = p.id
            JOIN testapp_category c ON p.category_id_id = c.id
            where sr.product_id_id = {};
        """.format(id)

        cursor.execute(sql_query)
        columns = [col[0] for col in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return result




def custom_sql_query():
    with connection.cursor() as cursor:
        
        sql_query = """
            SELECT sr.product_id_id,
                   p.name AS product_name,
                   p.product_unq_number,
                   c.name AS category_name,
                   SUM(CASE WHEN sr.type = 'PS' THEN sr.quantity ELSE 0 END) AS num_of_quantity_purchase,
                   SUM(CASE WHEN sr.type = 'OS' THEN sr.quantity ELSE 0 END) AS opening_stock,
                   SUM(CASE WHEN sr.type = 'SS' THEN sr.quantity ELSE 0 END) AS num_of_quantity_sale,
                   SUM(sr.quantity) AS quantity_onhand
            FROM testapp_stockreport sr
            JOIN testapp_product p ON sr.product_id_id = p.id
            JOIN testapp_category c ON p.category_id_id = c.id
            GROUP BY sr.product_id_id, p.name, c.name  order by sr.product_id_id;
        """

        cursor.execute(sql_query)
        columns = [col[0] for col in cursor.description]
        
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return result


class Purchase(APIView):
    def post(self,request):
        data = request.data 
        print(data)
        #import pdb;pdb.set_trace()
        status_code = status_code = status.HTTP_201_CREATED

        for i in data:
        
            product_instance = product.objects.get(pk=i.get("product_id"))
            purchase_inst = PurchaseOrder(description=i.get("description"))
            purchase_inst.save()

            product_purchase_inst = ppos( product_id= product_instance,purchase_id=purchase_inst,quantity=i.get('quantity'))
            product_purchase_inst.save()


            stock_report_inst = StockReport(description=i.get("description"), product_id =product_instance, type='PS', quantity=i.get('quantity'))
            stock_report_inst.save()
        return Response({"data":"purchase is added succefully"},status=status_code)

class Sale(APIView):
    def post(self,request):
        data = request.data 
        status_code = status_code = status.HTTP_201_CREATED

        for i in data:
        
            product_instance = product.objects.get(pk=i.get("product_id"))
            sale_inst = SalesOrder(description=i.get("description"))
            sale_inst.save()

            product_purchase_inst = ssos( product_id= product_instance,sale_id=sale_inst,quantity=i.get('quantity'))
            product_purchase_inst.save()

            stock_report_inst = StockReport(description=i.get("description"), product_id =product_instance, type='SS', quantity=-(i.get('quantity')))
            stock_report_inst.save()
        return Response({"data":"sale is added succefully"},status=status_code)

class StockReportOfsingleObject(APIView):
    def get(self,request,id):
        data  = single_object(id)
       
        for i in data:
            
            i["num_of_quantity_sale"] = abs(i["num_of_quantity_sale"])
        return Response({"data":data})
    

class StockReportS(APIView):
    def get(self,request):
        data = custom_sql_query()
        for i in data:
            i["num_of_quantity_sale"] = abs(i["num_of_quantity_sale"])
        return Response({"data":data})
class ProductView(APIView):
    def get(self,request):
        products = product.objects.all()
        data = ProductSerializer(products,many=True)
        return Response({"data":data.data})
        
    
    def post(self,request):
        data = request.data
        
        print(data)
        status_code = status.HTTP_201_CREATED
        
        inst = ProductSerializer(data=request.data)

       
        message = ""
        if inst.is_valid():
            ser = inst.save()
            print(ser.id)

            ser.productcost_set.create(cost=request.data.get('cost'))
            ser.stock_set.create(quantity=request.data.get('quantity'))
            stock_report_inst = StockReport(description="opesningstock in added", product_id =ser, type='OS', quantity=data.get('quantity'))
            
            stock_report_inst.save()

            message = "Data added successfully"
            data["id"] = ser.id
        else :
            message = "sorry....! Data not added"
            status_code = status.HTTP_404_NOT_FOUND
        return Response({"message":message,"product_id":data.get("id")},status=status_code)

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


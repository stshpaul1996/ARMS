from django.shortcuts import render
from .models import Customer, Orders

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import json

class SampleView(APIView):
    def get(self, request):
        return Response("get")
    
    def post(self, request):
        return Response("post")
    

class OrdersView(APIView):

    def get(self, request):
        db_data = Orders.objects.all()
        all = [ {"customer_id":i.customer_id.id,"customer_name":i.customer_id.name, "order_name":i.order_name, "price":i.price, 
           "descrpition":i.descrpition, "location":i.location} for i in db_data]
    
        return Response(all)

    def post(self, request):
        body = json.loads(request.body)
        get_id = Customer.objects.get(id=body.get("customer_id"))

        rd = request.data
        order = Orders(order_name=rd.get("order_name"), price=rd.get("price"),
        descrpition=rd.get("descrpition"), location=rd.get("location"), customer_id=get_id)
        msg = ""
        try:
            order.save()
            msg="You have successfully placed order"
        except Exception as err:
            msg = err
        
        return Response(msg)

class CustomerView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            user = Customer.objects.get(id=pk)
            customers_data = {
                "id":pk,
                "name":user.name,
                "phone":user.phone,
                "email":user.email,
                "address":user.address,
            }
        else:
            customers = Customer.objects.all()
            customers_data = [ { "id":customer.id, "name":customer.name,"phone":customer.phone ,"email":customer.email, 
                                "address":customer.address} for customer in customers]
        
        return Response(customers_data)
    


    def post(self,request):
        rd = request.data
        customer = Customer(name=rd.get("name"), phone=rd.get("phone"),
                           email=rd.get("email"), address=rd.get("address"))
        
        msg = ""
        try:
            customer.save()
            msg = "You have successfully registered"
        except Exception as err:
            msg = str(err)
        return Response(msg)
    

        
    def put(self, request, pk):
        data = json.loads(request.body) #dump
        modal_data = Customer.objects.get(id=pk)

        for key, value in data.items():
            if hasattr(modal_data, key):  
                setattr(modal_data, key, value)
        
        msg= ""
        try:
            modal_data.save()
            msg="You have successfully Updated"
        except Exception as err:
            msg = err

        return Response(msg)
    

    
    def delete(self, request, pk):
        instance = Customer.objects.get(id=pk)
        msg=""
        try:
            instance.delete()
            msg="Successfully deleted"
        except Exception as err:
            msg = str(err)
        return Response(msg)



        

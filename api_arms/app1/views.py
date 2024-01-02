from django.shortcuts import render

# Create your views here.

from .models import Employee,Department 
from rest_framework.views import APIView
from rest_framework.response import Response


class department_view(APIView):

    def get(self,request):
        data = Department.objects.all()
        data = [{'name':i.name,'description':i.description} for i in data]
        return Response(data)
    
    def post(self,request):
        data  = request.data
        cus_ins = Department(name = data['name'],description = data['description'])
        cus_ins.save()
        return Response("Data added successfully")
    
    # def put(self,request,id):
        
    #     dept = Department.objects.get(id =id )
    #     for key,value in request.body.data.items():
    #         if hasattr(dept,key):
    #             setattr(dept,key,value)
    #     dept.save()
        
    #     return Response("Record deleted successfully")
    
    def put(self, request, id):
        
        dept = Department.objects.get(id=id)
        
        for key in request.data:
            if hasattr(dept, key):
                setattr(dept, key, request.data[key])

        dept.save()
        return Response("Record updated successfully")
    
    def delete(self,request,id):
        data = request.data
        query = Department.objects.get(id = id)
        for key in data:
            if hasattr(query,key):
                delattr(query,key)
        query.save()
        return Response("Data deleted successfullt ")
    
    
     
class employee_view(APIView):


    def get(self,request):
        data = Employee.objects.all()
        data = [{'name':i.name,'email_id':i.email_id,'phone_number':i.phone_number,'address':i.address,'department':i.department.id} for i in data]
        return Response(data)
    

    def post(self,request):
        data  = request.data
        #dept = data['department']
        
        dep = Department.objects.get(id = data['department'])
        
        cus_ins = Employee(name = data['name'],email_id = data['email_id'],phone_number=data['phone_number'],address = data['address'],department=dep)
        cus_ins.save()
        return Response("Data added successfully")
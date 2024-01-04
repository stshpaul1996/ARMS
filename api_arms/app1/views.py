from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import Department, Employee
from app1.serialaizers import EmployeeSerialzer, DepartmentSerialzer
from rest_framework import status

# Create your views here.
class SampleView(APIView):
    def get(self,request):
        return Response('Get')
    
    def post(self,request):
        return Response('Post')
    
class Departments(APIView):
    def get(self,request):
        data = Department.objects.all()
        # data = [{'name':i.name,'description':i.description} for i in data]
        ser = DepartmentSerialzer(data, many=True)
        data = ser.data
        return Response(data)
    
    def post(self,request):
        # data  = request.data
        # cus_ins = Department(name = data['name'],description = data['description'])
        # cus_ins.save()
        ser = DepartmentSerialzer(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response("Data added successfully")

class Employees(APIView):
    def post(self,request):
        message =""
        # data = request.data
        # dep = Department.objects.get(id = data['department'])
        # emp = Employee(name = data['name'],email_id = data['email_id'],phone_number=data['phone_number'],address = data['address'],department=dep)
        # emp.save()
        ser = EmployeeSerialzer(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response("Data added successfully", status= status.HTTP_201_CREATED)

    def get(self,request):
        data = Employee.objects.all()
        # data1 = [{'name':i.name,'email_id':i.email_id,'phone_number':i.phone_number,'address':i.address,'department':i.department.id} for i in data]
        ser = EmployeeSerialzer(data, many= True)
        data = ser.data
        return Response(data)
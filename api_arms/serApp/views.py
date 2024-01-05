from django.shortcuts import render
from .ser import EmployeeSerializer, DepartmentSerializer
from .models import Employee, Department

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class EmployeeView(APIView):
    def post(self,request):
        ser=EmployeeSerializer(data=request.data)
        if ser.is_valid():
            #import pdb;pdb.set_trace()
            name_exists = Employee.objects.get(name=request.data.get('name')).exists()
            if name_exists==True:
                ser.save()
                response_data=ser.data 
                message="inserted successfully"
                return Response({"Result":message,"data":response_data})
            else:
                message="already exist "
                return Response({"Result":message})
        else:
            return Response(ser.errors)
    
    def get(self, request):
        data = Employee.objects.all()
        res = EmployeeSerializer(data, many=True)
        return Response(res.data)
    
    def patch(self, request, id):
        ins = Employee.objects.get(id=id)
        res = EmployeeSerializer(ins, data=request.data, partial=True)
        msg = ""
        if res.is_valid():
            res.save()
            msg = "updated successfully"
        else:
            msg = res.errors

        return Response(msg)    
    def delete(self, request, id):
        ins = Employee.objects.get(id=id)
        ins.delete()
        return Response("deleted successfully")


class DepartmentView(APIView):
    def post(self, request):
        dept = DepartmentSerializer(data=request.data)
        data = {}
        if dept.is_valid():
            dept.save()
            msg = "inserted successfully"
            code = status.HTTP_201_CREATED
            data = dept.data
        else:
            msg = dept.errors
            code = status.HTTP_400_BAD_REQUEST
        return Response({"res":msg, "data":data}, status=code)
    
    def get(self, request):
        data = Department.objects.all()
        res = DepartmentSerializer(data, many=True)
        return Response(res.data)
    
    def patch(self, request, id):
        ins = Department.objects.get(id=id)
        res = DepartmentSerializer(ins, data=request.data, partial=True)
        msg=""
        if res.is_valid():
            res.save()
            msg = "Updated successfully"
        else:
            msg=res.errors
        return Response(msg)
    
    def delete(self, request,id):
        ins = Department.objects.get(id=id)
        msg = ""
        try:
            ins.delete()
            msg = "deleted successfully"
        except Exception as err:
            msg = err
        return Response(msg)



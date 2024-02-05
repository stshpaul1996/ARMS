from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Employee, Department
from . serializers import EmployeeSerializer,DepartmentSerializer
from rest_framework import status

# Create your views here.
class EmployeeAPIView(APIView):
    def get(self,request, pk=None):
        if pk:
            employee=Employee.objects.get(pk=pk) #list of Employee instance
            serializer=EmployeeSerializer(employee) #dict of employee instance
        else:
            employee=Employee.objects.all()
            serializer=EmployeeSerializer(employee,many=True)
        return Response(serializer.data)

    
    def post(self,request, *args,**kwargs):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self,request,pk):
        employee=Employee.objects.get(pk=pk)
        serializer=EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk):
        employee=Employee.objects.get(pk=pk)
        serializer=EmployeeSerializer(employee,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        employee=Employee.objects.get(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class DepartmentAPIView(APIView):
    def get(self,request,pk=None):
        if pk:
            department=Department.objects.get(pk=pk)
            serializer=DepartmentSerializer(department)
        else:
            department=Department.objects.all()
            serializer=DepartmentSerializer(department,many=True)
        return Response(serializer.data)
        

    def post(self,request):
        serializer=DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        department=Department.objects.get(pk=pk)
        serializer=DepartmentSerializer(department,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        department=Department.objects.get(pk=pk)
        serializer=DepartmentSerializer(department,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        department=Department.objects.get(pk=pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        




    


<<<<<<< HEAD
=======
from django.shortcuts import render
from arms_api.application.models import Department, Employee
>>>>>>> 7cddd1a6d8b4c25cbb443e8281aa1a3452c5f16a
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Employee,Department
import json
# Create your views here.

class SampleView(APIView):
    def get(self, request, *args, **kwargs):
        return Response("get")
    
    def post(self, request, *args, **kwargs):
        return Response("post")

    def put(self, request, *args, **kwargs):
        return Response("put")
    
    def patch(self, request, *args, **kwargs):
        return Response("patch")
    
<<<<<<< HEAD
    def delete(self, request, *args, **kwargs):
        return Response("delete")

class DepartmentView(APIView):
    def get(self, request, *args, **kwargs):
        db_data=Department.objects.all()
        all=[{"employee_id":i.emp_id.id,"employee_department":i.department,"employee_location":i.location} for i in db_data]
        return Response(all)
    
    def post(self, request, *args, **kwargs):
        body=json.loads(request.body)
        employee=Employee.objects.get(id=body.get('emp_id'))

        rd=request.data
        depart=Department(emp_id= employee,department=rd.get("department"),location=rd.get("location"))
        msg=""
        try:
            depart.save()
            msg="you have successfully added"
        except Exception as err:
            msg=err
        return Response(msg)
    
class EmployeeView(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            user=Employee.objects.get(id=pk)
            employee_data={
                "id":user.pk,
                "name":user.name,
                "age":user.age,
                "salary":user.salary
            }
        else:
            employee=Employee.objects.all()
            employee_data=[{"id":i.id,"name":i.name,"age":i.age,"salary":i.salary} for i in employee]
        return Response(employee_data)
    
    def post(self,request):
        rd=request.data
        employee=Employee(name=rd.get("name"),age=rd.get("age"),salary=rd.get("salary"))
        msg=""
        try:
            employee.save()
            msg="you have successfully added"
        except Exception as err:
            msg=str(err)
        return Response(msg)
    
    def put(self, request,pk):
        data=json.loads(request.body)
        modal_data=Employee.objects.get(id=pk)
        for i,j in data.items():
            if hasattr(modal_data,i):
                setattr(modal_data,i,j)
        msg=""
        try:
            modal_data.save()
            msg="you have successfully updated"
        except Exception as err:
            msg=err
        return Response(msg)

    def delete(self,request,pk):
        instance=Employee.objects.get(id=pk)
        msg=""
        try:
            instance.delete()
            msg="successfully deleted"
        except Exception as err:
            msg=str(err)
        return Response(msg)
    


=======
class EmployeeView(APIView):

    def post(self,request):
        msg=""
        try:
            e=Employee(name=request.data.get("name"),age=request.data.get("age"),
                       salary=request.data.get("salary"))
            dept_id=request.data.get("dept_id")
            dept_instance=Department.objects.get(pk=dept_id)
            e.dept_id=dept_instance
            e.save()
            msg=("inserted successfully")
        except Exception as err:
            msg=str(err)
        return Response({"msg":msg})
    
    def get(self,request):
        db_data=Employee.objects.all()
        all=[{"name":i.name,"age":i.age,"salary":i.salary,"dept_id":i.dept_id} for i in db_data]
        return Response(all)
    
    
>>>>>>> 7cddd1a6d8b4c25cbb443e8281aa1a3452c5f16a

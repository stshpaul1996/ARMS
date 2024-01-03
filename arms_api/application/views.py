from django.shortcuts import render
from arms_api.application.models import Department, Employee
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class SampleView(APIView):
    def post(self,request):
        return Response("post") #the consumer of the api is expecting json response
    
    def get(self,request,**kwargs):
        return Response("get")
    
    def delete(self,request,**kwargs):
        return Response("delete")
    
    def put(self,request,**kwargs):
        return Response("put")
      
    def patch(self,request,**kwargs):
        return Response("patch")
    
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
    
    
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import Person,Student
import json
# Create your views here.
class SampleView(APIView):
    def get(self,request):
        res=Person.objects.all()
        result1=[{"name":i.name,"email":i.email,"mobile_no":i.mobile_no,"location":i.location}for i in res]
        return Response({"result":result1})
    def post(self,request):
        person_instance=Person(name=request.data.get("name"),email=request.data.get("email"),
                               mobile_no=request.data.get("mobile_no"),location=request.data.get("location")).save()
        return Response("post successfully")
class StudentView(APIView):
    def post(self,request):
        data=json.loads(request.body)
        get_id = Person.objects.get(id=data.get("person_id"))
        Student_instance=Student(roll_number=request.data.get("roll_number"),branch=request.data.get("branch"),person_id=get_id).save()
        return Response("post success")   
    def get(self,request):
        a=Student.objects.all()
        result2=[{"roll_number":i.roll_number,"branch":i.branch,"person_id":i.person_id.name} for i in a]
        return Response({"result2":result2})
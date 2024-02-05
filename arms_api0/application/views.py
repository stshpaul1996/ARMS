from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Person,Student
# Create your views here.

class SampleView(APIView):
    def get(self, request, *args, **kwargs):
        person=Person.objects.all()
        print("The type of person is=",type(person))
        data=[{"name":i.name,"id":i.id} for i in person]
        return Response(data)
    
    def post(self, request, *args, **kwargs):
        message =""
        person_inst=Person(name=request.data.get("name"))
        try:
            person_inst.save()
            message = "inserted successfully"
        except Exception as err:
            message = str(err)
        return Response({"Result":message})

class StudentView(APIView):
    def get(self, request,pk=None, *args, **kwargs):
        if pk:
            student=Student.objects.get(pk=pk)
            result={"name":student.name,"age":student.age,"address":student.address}
            return Response({"result":result})
        else:
            student=Student.objects.all()
            result1=[{"name":i.name,"age":i.age,"address":i.address}for i in student]
            return Response({"result1":result1})
        
    def post(self,request):
        message=""
        student_instance=Student(name=request.data.get("name"),age=request.data.get("age"),address=request.data.get("address"))
        try:
            student_instance.save()
            message="message inserted successfully"
        except Exception as err:
            message=str(err)
        return Response({"message":message})
    


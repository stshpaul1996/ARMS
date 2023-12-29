from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import Person

# Create your views here.
class SampleView(APIView):
    def post(self, request):
        #request parser
        # data = request.data
        # print(type(data))
        # print(request.data
        message = ""
        person_inst = Person(name=request.data.get("name"))
        try:
            person_inst.save()
            message="inserted successfully"
        except Exception as err:
            message = str(err)
        return Response({"Result":message})

    def get(self, request):
        persons = Person.objects.all()
        #response parser
        data = [ {"name": rec.name, "id": rec.id} for rec in persons]
        return Response(data)
        # return Response(persons)
        

    def delete(self, request, **kwargs):
        return Response("delete")


    def update(self, request, **kwargs):
        return Response("update")
    
    def patch(self, request, **kwargs):
        return Response("patch")




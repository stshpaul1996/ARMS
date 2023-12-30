from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import Person
from app1.serializers import PersonSerializer
from rest_framework import status

# Create your views here.
class SampleView(APIView):
    def post(self, request):
        #request parser
        # data = request.data
        # print(type(data))
        # print(request.data
        message = ""
        data = {}
        # person_inst = Person(name=request.data.get("name"))
        # try:
        #     person_inst.save()
        #     message="inserted successfully"
        # except Exception as err:
        #     message = str(err)
        ser = PersonSerializer(data=request.data)
        status_code = status.HTTP_201_CREATED
        if ser.is_valid():
            person_inst = ser.save()
            data = ser.data
            message="inserted successfully"
        else:
            status_code = status.HTTP_400_BAD_REQUEST
        return Response({"Result":message,"data": data}, status=status_code)

    def get(self, request):
        persons = Person.objects.all()
        #response parser
        # data = [ {"name": rec.name, "id": rec.id} for rec in persons]
        ser = PersonSerializer(persons, many=True)
        data = ser.data
        return Response(data)
        # return Response(persons)
        

    def delete(self, request, **kwargs):
        return Response("delete")


    def update(self, request, **kwargs):
        return Response("update")
    
    def patch(self, request, **kwargs):
        return Response("patch")




from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import Person
from app1.serializers import (PersonSerializer, ProductModelSerializer,
                              CategoryModelSerializer)
from rest_framework import status

# Create your views here.

class CategoryView(APIView):
    def post(self, request):
        data = {}
        ser = CategoryModelSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            message = "inserted successfully"
            status_code = status.HTTP_201_CREATED
            data = ser.data
        else:
            message=ser.errors
            status_code = status.HTTP_400_BAD_REQUEST

        return Response({"Result":message,"data": data}, status=status_code)

class ProductView(APIView):
    def post(self, request):
        data = {}
        ser = ProductModelSerializer(request.data)
        #ser.instance # model instanc
        # product_model_instance.category.name
        if ser.is_valid():
            ser.save()
            message = "inserted successfully"
            status_code = status.HTTP_201_CREATED
            data = ser.data
        else:
            message=ser.errors
            status_code = status.HTTP_400_BAD_REQUEST

        return Response({"Result":message,"data": data}, status=status_code)
class SampleView(APIView):
    def post(self, request):
        message = ""
        data = {}
        ser = PersonSerializer(data=request.data)
        status_code = status.HTTP_201_CREATED
        if ser.is_valid():
            person_inst = ser.save()
            person_inst.created_by = request.user
            person_inst.save()
            data = ser.data
            message="inserted successfully"
        else:
            message=ser.errors
            status_code = status.HTTP_400_BAD_REQUEST
        return Response({"Result":message,"data": data}, status=status_code)

    def get(self, request):
        persons = Person.objects.all()
        query_params = request.query_params
        if query_params:
            if "name" in query_params:
                persons = persons.filter(name=query_params.get("name"))
            
        #response parser
        # data = [ {"name": rec.name, "id": rec.id} for rec in persons]
        ser = PersonSerializer(persons, many=True)
        data = ser.data
        return Response(data)
        # return Response(persons)
        

    def delete(self, request, **kwargs):
        return Response("delete")


    def put(self, request, pk, **kwargs):
        return Response("update")
    
    def patch(self, request, pk, **kwargs):
        return Response("patch")




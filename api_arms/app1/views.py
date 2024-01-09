from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import Person
from app1.serializers import (PersonSerializer, ProductModelSerializer,
                              CategoryModelSerializer,PoductCostOpeningstockSerializer)
from rest_framework import status

# Create your views here.

class PoductCostOpeningstockView(APIView):
    # def post(self,request):
    #     serilizer=PoductCostOpeningstockSerializer(data=request.data)
    #     if serilizer.is_valid():
    #         message='inserted success fully'
    #         status_code = status.HTTP_201_CREATED
    #     else :
    #         message=serilizer.errors
    #         status_code = status.HTTP_400_BAD_REQUEST
    #     return Response({"Result": message}, status=status_code)
    def post(self,request):
        serilizer =PoductCostOpeningstockSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            message='inserted success fully'
            status_code = status.HTTP_201_CREATED
        else :
            message=serilizer.errors
            status_code = status.HTTP_400_BAD_REQUEST
        return Response({"Result": message}, status=status_code)


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
        # import pdb;pdb.set_trace()
        if ser.is_valid():
            person_inst = ser.save()
            data = ser.data
            message="inserted successfully"
        else:
            message=ser.errors
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


    def put(self, request, pk, **kwargs):
        return Response("update")
    
    def patch(self, request, pk, **kwargs):
        return Response("patch")




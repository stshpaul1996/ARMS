from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView

class PersonView(APIView):
    def get(self,request):
        instance = Person.objects.all()
        ser = PersonSerializer(instance)
        return Response(ser.data)
    def post(self,request):
        ser = PersonSerializer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response("Data Added successfully")
        else:
            return Response(ser.data)
    def put(self,request):
        pass 
    def delete(self,request):
        pass 
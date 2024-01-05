from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Student 
from .serializers import studentserializer

class sampleView(APIView):
    def post(self,request):
        serz=studentserializer(data=request.data)
        if serz.is_valid():
            serz.save()
            return Response("data inserted successfully")
       # return Response(serz.data)
        return Response(serz.errors, status=400)
    def get(self,request):
        student=Student.objects.all()
        serz=studentserializer(student,many=True)
        d=serz.data
        return Response(d)
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
        return Response(serz.data)
    def get(self,request):
        student=Student.objects.all()
        serz=studentserializer(student,many=True)
        d=serz.data
        return Response(d)
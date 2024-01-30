from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Student

# Create your views here.

class StudentView(APIView):
    def post(self,request):
        message=''
        error=''
        data={}
        ser=StudentSerializer(data=request.data)
        status_code=status.HTTP_201_CREATED
        #import pdb;pdb.set_trace()
        if ser.is_valid():
            ser.save()
            data=ser.data
            message='instered successfully....!'
        else:
            error=ser.errors
            status_code=status.HTTP_400_BAD_REQUEST
        return Response({'Result=':message,'data':data,'error':error},status=status_code)
    
    def get(self,request):
        students=Student.objects.all()
        ser=StudentSerializer(students,many=True)
        data=ser.data
        return Response(data)
    


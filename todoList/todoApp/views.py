from django.shortcuts import render

# Create your views here.

from rest_framework.views  import APIView
from rest_framework.response import Response 
from .serializers import TaskSerializer
from .models import Task


class TodosView(APIView):
    def get(self,request,id = None):
        if id != None:
            ins = Task.objects.get(id = id)
            ser = TaskSerializer(ins)
            return Response(ser.data)
        else:

            tasks = Task.objects.all()
            ser = TaskSerializer(tasks,many=True)
            return Response(ser.data)
        


    def post(self,request):
        ser = TaskSerializer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    
    def put(self,request,id):
        ins = Task.objects.get(id = id)
        ser = TaskSerializer(ins,data = request.data)
        # for key in request.data:
        #     if hasattr(ins,key):
        #         setattr(ins,key,request.data[key])
        #         return Response("updated successfully")
        if ser.is_valid():
            ser.save()
            return Response("updated Successfully")
        return Response(ser.errors)
    
    def delete(self,request,id):
        ins = Task.objects.get(id = id)
        ins.delete()
        return Response("Data Deleted Successfully")
        






    


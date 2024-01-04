from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Person
from app.serializers import PersonSerializer

# Create your views here.
class SampleView(APIView):
    def post(self,request):
        ser=PersonSerializer(data=request.data)
        #import pdb;pdb.set_trace()
        if ser.is_valid():
            find = ser.validated_data.get('name')
            print(find)
            if Person.objects.filter(name=find).exists():
                return Response({"error": "Person with this name already exists"})
            person_instance=ser.save()
            res=ser.data 
        else:
            res=ser.errors
        return Response({"res":res})
    def get(self,request):
        persons=Person.objects.all()
        ser=PersonSerializer(persons,many=True)
        data=ser.data 
        return Response(data)
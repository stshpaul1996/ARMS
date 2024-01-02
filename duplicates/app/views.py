from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from app.models import Person
from app.serializers import PersonSerializer
# Create your views here.
class SampleView(APIView):
    def post(self,request):
        ser=PersonSerializer(data=request.data)
        if ser.is_valid():
            name_exists = Person.objects.filter(name=request.data.get('name')).exists()
            if name_exists==False:
                person_instance=ser.save()
                response_data=ser.data 
                message="inserted successfully"
                return Response({"Result":message,"data":response_data})
            else:
                message="already exist "
                return Response({"Result":message})
        else:
            print(ser.errors)
    def get(self,request):
        persons=Person.objects.all()
        ser=PersonSerializer(persons,many=True)
        data=ser.data
        return Response(data)
        


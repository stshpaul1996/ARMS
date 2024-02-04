from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
import datetime

from .serializers import *
from .models import *
from .authentication import users

class TripView(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def perform_create(self, serializer):

        validated_data = serializer.validated_data
        validated_data["created_by"] = users["user"]
        serializer.save()
        
    
    def perform_update(self, serializer):
        validated_data = serializer.validated_data
        validated_data["updated_by"] = users["user"]
        validated_data["updated_at"] = datetime.datetime.now()
        serializer.save()
       


class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        validated_data["created_by"] = users["user"]
        serializer.save()
    
    def perform_update(self, serializer):
        validated_data = serializer.validated_data
        validated_data["updated_by"] = users["user"]
        validated_data["updated_at"] = datetime.datetime.now()
        serializer.save()
      


class ExpensesView(APIView):
    def post(self, request):
        req_data = request.data
        req_data["created_by"] = users["user"]
        req = ExpensesSerializer(data=req_data)
        msg = ""
        if req.is_valid():
            req.save()
            msg = "Added Successfully"
            status_code = status.HTTP_201_CREATED
        else:
            msg = req.errors
            status_code = status.HTTP_400_BAD_REQUEST
        
        return Response({"Result":msg, "data":request.data}, status=status_code)
    
    def get(self, request, id=None):
        if id == None:
            # data = Expenses.objects.all()
            # res = ExpensesSerializer(data, many=True)
            # return Response(res.data)

            data = []
            for i in Member.objects.all():
                persons = {}
                for j in Expenses.objects.all():
                    if i.id == j.member_id:
                        persons["name"] = i.name
                        if "spent" in persons:
                            persons["spent"] += j.spent
                        else:
                            persons["spent"] = j.spent 
                    else:
                        pass
                data.append(persons)
        




        
            
            return Response(data)

        else:
            data = Expenses.objects.get(id=id)
            res = ExpensesSerializer(data)
            return Response(res.data)

    


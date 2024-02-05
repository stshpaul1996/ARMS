from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.db.models import Avg, Count, Sum
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


    # def list(self, request, *args, **kwargs):
    #     pass

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        validated_data["created_by"] = users["user"]
        serializer.save()
    
    def perform_update(self, serializer):
        validated_data = serializer.validated_data
        validated_data["updated_by"] = users["user"]
        validated_data["updated_at"] = datetime.datetime.now()
        serializer.save()
      


class ExpensesView(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print(serializer.data)
        id = serializer.data['id']
        print(id)
        data = Member.objects.filter(trip=id)
        total_members = len(data)
        mem_id = 0
        for i in data:
            mem_id = i.id
            break
        print(mem_id)
        expenses = Expenses.objects.filter(member=mem_id).aggregate(Sum('spent'))
        print(expenses)
        try:
            each_person_expenses = expenses['spent__sum']/total_members
        except Exception as err:
            return Response({})
        members = []
        for i in data:
            members.append(i.name)
       

        return Response({'trip':id,'members':members, 'total':expenses['spent__sum'], 'each_person_expenses':each_person_expenses})




    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        validated_data["created_by"] = users["user"]
        serializer.save()
    
    def perform_update(self, serializer):
        validated_data = serializer.validated_data
        validated_data["updated_by"] = users["user"]
        validated_data["updated_at"] = datetime.datetime.now()
        serializer.save()
      



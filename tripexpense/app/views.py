from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Trip, Member, Expense
from .serializers import TripSerializer, MemberSerializer, ExpenseSerializer
from django.db.models import Sum

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def list(self, request):
        trip_id = request.query_params.get('tripid')
        member_id = request.query_params.get('memberid')
        member_name = request.query_params.get('membername')
        if not trip_id:
            return Response({'error': 'Trip ID is required query parameter'}, status=400)

        try:
            total_expenses = Expense.objects.filter(trip_id=trip_id).aggregate(total=Sum('amount'))['total']
            total_members = Member.objects.filter(trip_id=trip_id).count()

            if total_expenses is None or total_members == 0:
                return Response({'error': 'No expenses or members found for the trip'}, status=404)

            if member_id:
                member_expenses = Expense.objects.filter(trip_id=trip_id, member_id=member_id).aggregate(total=Sum('amount'))['total']
                if member_expenses is None:
                    member_expenses = 0
                member_share = total_expenses / total_members
                return Response({'member_share': member_share, 'member_expenses': member_expenses})

            member_share = total_expenses / total_members
           # return Response({'member_share': member_share})
            if member_name:
                member_expenses = Expense.objects.filter(trip_id=trip_id, member_name=member_name).aggregate(total=Sum('amount'))['total']
                if member_expenses is None:
                    member_expenses = 0
                member_share = total_expenses / total_members
                return Response({'member_share': member_share, 'member_expenses': member_expenses})

            member_share = total_expenses / total_members
            return Response({'member_share': member_share})
        except Expense.DoesNotExist:
            return Response({'error': 'Expenses not found'}, status=404)
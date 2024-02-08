from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Member, Expense, Trip
from .serializers import MemberSerializer, ExpenseSerializer, TripSerializer
from datetime import datetime


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        is_creation = instance.pk is None
        user_updating = self.request.user
        updated_date_str = datetime.now().isoformat() + "Z"
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            created_by=user_updating if is_creation else instance.created_by,
            updated_by=user_updating,
            updated_date=updated_date_str)
        return Response(serializer.data)

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        is_creation = instance.pk is None
        user_updating = self.request.user
        updated_date_str = datetime.now().isoformat() + "Z"
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            created_by=user_updating if is_creation else instance.created_by,
            updated_by=user_updating,
            updated_date=updated_date_str)
        return Response(serializer.data)

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    print(queryset)
    serializer_class = TripSerializer
    print(serializer_class)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Calculate member shares and add them to the response data
        member_shares = instance.calculate_member_shares()
        print(member_shares)
        serializer_data = serializer.data
        print(serializer_data)
        serializer_data['member_shares'] = member_shares

        return Response(serializer_data)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        is_creation = instance.pk is None
        user_updating = self.request.user
        updated_date_str = datetime.now().isoformat() + "Z"
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            created_by=user_updating if is_creation else instance.created_by,
            updated_by=user_updating,
            updated_date=updated_date_str)
        return Response(serializer.data)

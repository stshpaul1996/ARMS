from django.shortcuts import render

# # Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import Vehicle, Trip
from .serializers import VehicleSerializer, TripSerializer
from django.utils.dateparse import parse_date
from rest_framework.permissions import IsAuthenticated
from .authentication import *

class VehicleViewSet(viewsets.ModelViewSet):
    #permission_classes = []
    #authentication_classes = []

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.id)


    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user.id)
        serializer.save(updated_by=self.request.user.id)

class TripViewSet(viewsets.ModelViewSet):
    # permission_classes = []
    #authentication_classes = []

    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    # def create(self, request, *args, **kwargs):
    #     data=request.data
    #     data["created_by"]=request.user.id
        
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
   
    # def update(self, request, *args, **kwargs):
    #     data=request.data
    #     data["updated_by"]=request.user.id
    #     print(data)
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
 
    #     queryset = self.filter_queryset(self.get_queryset())
        
 
    #     return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        #import pdb;pdb.set_trace()
        data = request.data
        #data["created_by_name"] = request.user.get('username')  
        data["created_by"] = request.user.get('user_id')  
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def update(self, request, *args, **kwargs):
        data = request.data
        #data["updated_by_name"] = request.user.get('username')  
        data["updated_by"] = request.user.get('user_id')
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
 
        queryset = self.filter_queryset(self.get_queryset())
        
 
        return Response(serializer.data)

    # def perform_create(self, serializer):
        
    #     username = self.request.user.username
    #     serializer.save(created_by=username)

    # def perform_update(self, serializer):
    #     username = self.request.user.username
    #     serializer.save(updated_by=username)

class AvailableVehiclesViewSet(viewsets.ViewSet):
    #permission_classes = []
   # authentication_classes = []
    def list(self, request):
        num_of_people = request.query_params.get('num_of_people', 1)
        date_str = request.query_params.get('date')
        date = parse_date(date_str) if date_str else None
        
        
        available_vehicles = Vehicle.objects.filter(capacity__gte=num_of_people)

        
        if date:
            trips = Trip.objects.filter(start_date=date, end_date=date)
            vehicle_ids_on_trip = trips.values_list('vehicle_id', flat=True)
            available_vehicles = available_vehicles.exclude(id__in=vehicle_ids_on_trip)

        
        serializer = VehicleSerializer(available_vehicles, many=True)

        return Response({'available_vehicles': serializer.data})




# import jwt
# from django.conf import settings
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Trip, Vehicle
# from .serializers import TripSerializer, VehicleSerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import BaseAuthentication
# from rest_framework.exceptions import AuthenticationFailed
# from jwtAuthentication import *


# class TripView(APIView):
#     permission_classes = [IsAuthenticated]
#     #authentication_classes = []

#     def get(self, request):
#         trips = Trip.objects.all()
#         serializer = TripSerializer(trips, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         request.data['created_by'] = request.user
#         serializer = TripSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         trip = Trip.objects.get(pk=pk)
#         request.data['updated_by'] = request.user
#         serializer = TripSerializer(trip, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         trip = Trip.objects.get(pk=pk)
#         request.data['updated_by'] = request.user
#         serializer = TripSerializer(trip, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         trip = Trip.objects.get(pk=pk)
#         trip.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# # fleet/views.py

# class VehicleView(APIView):
#     permission_classes = [IsAuthenticated]
#     #authentication_classes = []

#     def get(self, request):
#         vehicles = Vehicle.objects.all()
#         serializer = VehicleSerializer(vehicles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         request.data['created_by'] = request.user
#         serializer = VehicleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         vehicle = Vehicle.objects.get(pk=pk)
#         request.data['updated_by'] = request.user
#         serializer = VehicleSerializer(vehicle, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         vehicle = Vehicle.objects.get(pk=pk)
#         request.data['updated_by'] = request.user
#         serializer = VehicleSerializer(vehicle, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         vehicle = Vehicle.objects.get(pk=pk)
#         vehicle.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# class AvailableVehicles(APIView):
#     permission_classes = [IsAuthenticated]
#     #authentication_classes = []

#     def get(self, request):
#         num_of_people = request.query_params.get('num_of_people', 1)
#         date_str = request.query_params.get('date')
#         date = parse_date(date_str) if date_str else None
        
        
#         available_vehicles = Vehicle.objects.filter(capacity__gte=num_of_people)

       
#         if date:
#             trips = Trip.objects.filter(start_date__lte=date, end_date__gte=date)
#             vehicle_ids_on_trip = trips.values_list('vehicle_id', flat=True)
#             available_vehicles = available_vehicles.exclude(id__in=vehicle_ids_on_trip)

       
#         serializer = VehicleSerializer(available_vehicles, many=True)

#         return Response({'available_vehicles': serializer.data})



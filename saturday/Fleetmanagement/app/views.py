from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from app.models import * 
from app.serializers import *
from django.db.models import Count
from django.utils.dateparse import parse_date
# Create your views here.
from django.db.models import Q

# class AvailableVehicleAPIView(APIView):
#     # def get(self, request):
#       def get(self, request, id, *args, **kwargs):  
#         import pdb;pdb.set_trace()
#         # date = request.query_params.get('date')
#         # num_seats = request.query_params.get('num_seats')
#         s_date=Trip.objects.get(id=id)
#         e_date=Trip.objects.get(id=id)
#         num_seats=Trip.objects.get(id=id)
#         if not date or not num_seats:
#             return Response({"detail": "Please provide both date and num_seats parameters"},
#                             status=status.HTTP_400_BAD_REQUEST)

#         # Assuming date is in the format 'YYYY-MM-DD'
#         # Get the list of available vehicles based on the date and number of seats
#         available_vehicles = Vehicle.objects.filter(
#             ~Q(trip__start_date__lte=date, trip__end_date__gte=date),  # Exclude vehicles that are booked on the given date
#             no_of_seats__gte=num_seats
#         )
#         print(available_vehicles)
#         serializer = VehicleSerializer(available_vehicles, many=True)
#         return Response(serializer.data)
    

# class AvailableVehicleAPIView(APIView):
#        def get(self, request):
#         num_of_people = request.query_params.get('num_of_people', 1)
#         date_str = request.query_params.get('date')
#         date = parse_date(date_str) if date_str else None
            
#         available_vehicles = Vehicle.objects.filter(no_of_seats__gte=num_of_people)
#         print(available_vehicles)
        
            
#         if date:
#             trips = Trip.objects.filter(start_date=date, end_date=date)
#             print(trips,"ttttttttt")
#             vehicle_ids_on_trip = trips.values_list('vehicles_id', flat=True)
#             print(vehicle_ids_on_trip,"vvvvvvvvvvvvvvvvv")
#             available_vehicles = available_vehicles.exclude(id__in=vehicle_ids_on_trip)
#             print(available_vehicles,"aaaaaaaaaaaaaaaa")
#             serializer = VehicleSerializer(available_vehicles, many=True)
#             return Response({'available_vehicles': serializer.data})    




class AvailableVehicleAPIView(APIView):
    def get(self, request):
        date = request.query_params.get('date')
        num_seats = request.query_params.get('num_seats')
      
        if not date or not num_seats:
            return Response({"detail": "Please provide both date and num_seats parameters"},status=status.HTTP_400_BAD_REQUEST)

        # Assuming date is in the format 'YYYY-MM-DD'
        # Get the list of available vehicles based on the date and number of seats
        available_vehicles = Vehicle.objects.filter(
            ~Q(trip__start_date__lte=date, trip__end_date__gte=date),  # Exclude vehicles that are booked on the given date
            no_of_seats__gte=num_seats
        )
        # print(available_vehicles)
        serializer = VehicleSerializer(available_vehicles, many=True)
        return Response(serializer.data)
    
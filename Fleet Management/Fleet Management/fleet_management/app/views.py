from .models import Vehicle_category,Vehicle, Trip
from .serializers import VehicleCategorySerializer,VehicleSerializer, TripSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.authentication import BasicAuthentication
from django.http import Http404
from django.utils import timezone


class AvailableVehiclesAPIView(APIView):

    def get(self, request):
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        num_of_people = request.data.get('num_of_people')

        if start_date and end_date and num_of_people:
            available_vehicles = Vehicle.objects.exclude(
                Q(trip__start_date__lte=start_date, trip__end_date__gte=end_date) |
                Q(trip__start_date__gte=start_date, trip__end_date__lte=end_date) |
                Q(trip__start_date__lte=start_date, trip__end_date__gte=start_date) |
                Q(trip__start_date__lte=end_date, trip__end_date__gte=end_date)
            ).filter(type_of_vehicle__no_of_seats__gte=num_of_people).distinct()
            serializer = VehicleSerializer(available_vehicles, many=True)
            return Response(serializer.data)
        else:
            return Response("Missing query parameters", status=status.HTTP_400_BAD_REQUEST)

class AllocateVehicleAPIView(APIView):
    def post(self, request):
        data = request.data
        data['created_by'] = str(request.user.get('username'))
        serializer = TripSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Trip.objects.get(pk=pk)
        except Trip.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        trip = self.get_object(pk)
        serializer = TripSerializer(trip)
        return Response(serializer.data)
    def get(self):
        trip = Trip.objects.all()
        serializer = TripSerializer(trip)
        return Response(serializer.data)

    def put(self, request, pk):
        trip = self.get_object(pk)
        data = request.data
        data['updated_by'] = str(request.user.get('username'))
        data['updated_at'] = timezone.now()
        serializer = TripSerializer(trip, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        trip = self.get_object(pk)
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class RegisterVehicleAPIView(APIView):
    def post(self, request):
        data=request.data
        data['created_by']=str(request.user.get('username'))
        print(request.user)
        serializer = VehicleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        vehicle = self.get_object(pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)
    def get(self):
        vehicle = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    def put(self, request, pk):
        vehicle = self.get_object(pk)
        data = request.data
        data['updated_by'] = str(request.user.get('username'))
        data['updated_at'] = timezone.now()
        serializer = VehicleSerializer(vehicle, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        vehicle = self.get_object(pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class VehicleCategoryViewSet(viewsets.ModelViewSet):
    queryset = Vehicle_category.objects.all()
    serializer_class = VehicleCategorySerializer

    def create(self, request, *args, **kwargs):
        # Ensure that created_by is set before creating the instance
        if not request.data.get('created_by', None):
            request.data['created_by'] = request.user.get('username')
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # Ensure that updated_by is set before updating the instance
        if not request.data.get('updated_by', None):
            request.data['updated_by'] = request.user.get('username')
            request.data['updated_at'] = timezone.now()
        return super().update(request, *args, **kwargs)

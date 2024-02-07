from rest_framework import serializers
from .models import Vehicle, Trip

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'vehicle_name', 'vehicle_type', 'capacity', 'created_by', 'created_at', 'updated_at', 'updated_by']

class TripSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trip
        fields = ['id', 'vehicle', 'start_date', 'end_date', 'num_of_people', 'created_by', 'created_at', 'updated_at', 'updated_by']

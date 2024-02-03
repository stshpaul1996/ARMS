from rest_framework import serializers
from .models import Vehicle_category, Vehicle, Trip

class VehicleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_category
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

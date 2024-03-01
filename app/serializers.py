from rest_framework import serializers
from app.models import *

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicle 
        fields="__all__"

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trip 
        fields="__all__"


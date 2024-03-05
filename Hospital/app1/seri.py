from rest_framework import serializers
from .models import *

class Hosptials(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class Doctors(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class Schedules(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
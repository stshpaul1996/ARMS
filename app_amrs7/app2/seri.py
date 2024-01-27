from rest_framework import serializers
from .models import *

class Persons(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class Departments(serializers.ModelSerializer):
    class Meta:
        model = Department
        fileds = '__all__'
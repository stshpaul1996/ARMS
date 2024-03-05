from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .seri import *
from .models import *
# Create your views here.

class Hosptialv(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = Hosptials

class Doctorv(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = Doctors

class Schedulev(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = Schedules
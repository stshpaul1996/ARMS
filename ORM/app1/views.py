from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .seri import *
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Max, F, Q
from django.db.models.functions import Concat
# Create your views here.

class VisitV(APIView):

    def post(self, request):
        v = Visits(data=request.data)
        if v.is_valid():
            v.save()
            return Response(v.data, status=status.HTTP_201_CREATED)
        return Response(v.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):

        # g = Visit.objects.values('name').annotate(
        #     total_visits=Count('name'),
        #     most_visited_floor=Max('floor'),
        #     # resources=Concat('resource', distinct=True),
        # )

        g = Visit.objects.filter(
        Q(floor=3) &
    (
        Q(resource__icontains='CPU') |
        Q(resource__icontains='DESKTOP') |
        Q(resource__icontains='MONITOR') |
        Q(resource__icontains='Keyboard')
    )
)
        return Response(g)
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count,Min

# Create your views here.

class EmpViewsets(viewsets.ViewSet):
    serializer_class=EmployeeSerializer

    def list(self,request):
        queryset=Employee.objects.all()
        result = queryset.values('name').annotate(
            total_visits=Count('floor'),
            resources_used=Count('resources'))
        

        for item in result:
            resources = set(Employee.objects.filter(name=item['name']).values_list('resources', flat=True))
            item['resources_used'] = ', '.join(resources)
        

        # # Group by 'name' again to find the most visited floor for each person
        most_visited_floors = queryset.values('name').annotate(most_visited_floor=Min('floor'))

        # # Merge the two result sets
        for item in result:
            most_visited_floor = next(filter(lambda x: x['name'] == item['name'], most_visited_floors),
                                         {}).get('most_visited_floor')
            item['most_visited_floor'] = most_visited_floor
    
        return Response(result, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import viewsets 
from rest_framework.response import Response
from app.models import *
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED 
from app.serializers import *
from django.db.models.query import prefetch_related_objects

class VehicleViewSet(viewsets.ModelViewSet):
    queryset=Vehicle.objects.all()
    serializer_class=VehicleSerializer 

    def create(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()
        data=request.data
        data["created_by"]=request.user.id
        data["update_at"]=None
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
 
    def update(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()
        data=request.data
        data["update_by"]=request.user.id
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
 
        queryset = self.filter_queryset(self.get_queryset())
        if queryset._prefetch_related_lookups:
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance,
            # and then re-prefetch related objects
            instance._prefetched_objects_cache = {}
            prefetch_related_objects([instance], *queryset._prefetch_related_lookups)
 
        return Response(serializer.data)
      
class TripViewSet(viewsets.ModelViewSet):
    queryset=Trip.objects.all()
    serializer_class=TripSerializer

    def create(self, request, *args, **kwargs):
            # import pdb;pdb.set_trace()
            data=request.data
            data["created_by"]=request.user.id
            data["update_at"]=None
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def update(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()
        data=request.data
        data["update_by"]=request.user.id
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
 
        queryset = self.filter_queryset(self.get_queryset())
        if queryset._prefetch_related_lookups:
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance,
            # and then re-prefetch related objects
            instance._prefetched_objects_cache = {}
            prefetch_related_objects([instance], *queryset._prefetch_related_lookups)
 
        return Response(serializer.data)
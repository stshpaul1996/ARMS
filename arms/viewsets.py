from rest_framework import viewsets
from rest_framework.response import Response
from arms.serializers import *
from rest_framework.views import APIView
from arms.models import MyUser,Role,trip,expenses,member,Permission,Api
from django.db.models import Count


class SampleViewset(viewsets.ModelViewSet):
    
    queryset = MyUser.objects.all()
    serializer_class = SampleSerializer

class roleViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Role.objects.all()
    serializer_class = Roleserializer

class tripViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = trip.objects.all()
    serializer_class = TripSerializer


class memberViewSet(viewsets.ModelViewSet):
    queryset = member.objects.all()
    serializer_class = MemberSerializer

class expensesViewSet(viewsets.ModelViewSet):
    queryset = expenses.objects.all()
    serializer_class = ExpensesSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class ApiViewSet(viewsets.ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer

class TripExpenseView(APIView):
    def get(self,request,pid):
        location = expenses.objects.get(trip_id = pid) 
        a = trip.objects.get(id = pid).name
        
        total_mem = member.objects.filter(trip_id = pid).aggregate(total_count= Count('trip_id'))['total_count']
        for_each = location.total_amount / total_mem
        data = {"trip_name":a,"total_mem":total_mem,"total_expenses": location.total_amount,"for each total amount":for_each}
        return Response(data)

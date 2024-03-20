from . models import Employee
from . serializers import EmployeeSerializer
from rest_framework import viewsets

# Create your views here.
class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

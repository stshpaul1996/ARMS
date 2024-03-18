from rest_framework import viewsets
from . models import Employee
from . serializers import EmployeeSerializer
from rest_framework.response import Response

class EmployeeViewSet(viewsets.ModelViewSet):
    # queryset=Employee.objects.filter(eaddr="New Richardburgh")
    # queryset=Employee.objects.filter(esal__gt=19000)
    # queryset=Employee.objects.filter(esal__gte=19000)
    # queryset=Employee.objects.filter(esal__lt=11000)
    # queryset=Employee.objects.filter(esal__lte=11000)
    # queryset=Employee.objects.filter(id=10)
    # queryset=Employee.objects.filter(id__exact=11)
    # queryset=Employee.objects.filter(id__in=[1,5,10])
    # queryset=Employee.objects.filter(esal__range=[10000,10500])
    # queryset=Employee.objects.filter(ename__startswith="D")
    # queryset=Employee.objects.filter(ename__endswith="d")
    # queryset=Employee.objects.filter(ename__contains="New")
    # queryset=Employee.objects.filter(ename__icontains="Thomas")
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,pk=None,*args,**kwargs):
        if pk:
            employee=Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee)
        else:
            employee=Employee.objects.all()
            serializer = EmployeeSerializer(employee,many=True)
        return Response(serializer.data)
    

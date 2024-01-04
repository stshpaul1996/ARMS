from rest_framework import serializers
from app1.models import Employee, Department

class EmployeeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class DepartmentSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"
from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Employee, Department

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def validate_name(self, value=None):
        for i in value:
            if i.isupper():
                raise ValidationError("Contains upper case")
        return value.upper()

    
       

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

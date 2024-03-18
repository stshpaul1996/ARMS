from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    summ = serializers.SerializerMethodField()
    #summ is method field type
    class Meta:
        model = Employee
        fields = ("english","maths","science","summ")
        
    def get_summ(self, obj):
        # Define your logic to calculate the summ here
        return obj.summ
    
    # def get_summ(self, obj):
    #     # Define your logic to calculate the summ here
    #     return obj.english+obj.maths+obj.science
    
    

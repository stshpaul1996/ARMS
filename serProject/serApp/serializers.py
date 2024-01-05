from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

    def validate_name(self, value):
        
        if len(value)>5:
            raise serializers.ValidationError('enter 5 characters')

        return value.upper()
    
    def validate(self,data):
        #import pdb;pdb.set_trace()
        name = data.get('name')
        
        existing_student = Student.objects.filter(name=name).exists()
        if existing_student:
            raise serializers.ValidationError('A student with this name already exists.')
        return data
    
        
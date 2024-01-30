from rest_framework import serializers
from .models import Student
from django.core.exceptions import ValidationError

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'


    def validate_name(self, value):
        if value.isalnum():
            return value.upper()
        raise ValidationError('Enter more than 3 charaters')
        
    
    def validate_email(self, value=None):
       return value
    
    def validate_age(self,value=None):
        return value


    def validate(self, data):
        #import pdb;pdb.set_trace()
        data=self.initial_data
        ag=data.get('age')
        if ag  and int(ag)>=18:
            if not data.get('email'):
                raise ValidationError('Email is mandatory')
        return data 
            

from rest_framework import serializers
from app.models import Person
from django.core.exceptions import ValidationError

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'
    def validate_name(self,value):
        print(value)
        if value.isalpha():
            print("KKKKKKKKKKKKKKK")
            return value.upper()
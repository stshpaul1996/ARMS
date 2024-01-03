from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

    def validate_name(self,value=None):
        print('eeeeeeeeeeeeeeeeeee')
        if value.isalpha():
            print('ok')
            return value.upper()
        raise ValidationError('expecting only alphanumeric values')
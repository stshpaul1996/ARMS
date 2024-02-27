from rest_framework import serializers
from .models import ProxyStudentModel

class ProxyStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProxyStudentModel
        fields="__all__"

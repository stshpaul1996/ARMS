from .models import *

from rest_framework import serializers 
from app.serializers import *

class Proxyserializer(serializers.ModelSerializer):
    class Meta:
        model = Proxymodel
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        age = representation.get('age')
        if age is not None:
            modified_age = age + 10
            representation['age'] = modified_age
        return representation
    
    

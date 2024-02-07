from .models import * 
from rest_framework.views import serializers 

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__" 
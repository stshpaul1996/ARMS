from .models import *
from rest_framework import serializers
class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ['name','address','email','floor','resources']

    def create(self, validated_data):
        validated_data['resources'] = validated_data.get('resources').upper()
        
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        name = representation.get('name')
        resources = representation.get('resources')
        if name is not None:
            modified_name = "MR  " + name
            representation['name'] = modified_name
        representation['resources'] = resources.lower()
        return representation
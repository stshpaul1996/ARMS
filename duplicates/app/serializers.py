from rest_framework import serializers
from app.models import Person
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'


#what will happened inside when PersonSerializer class calls
# def Create(self, validated_data):
#     print(instance)
#     instance = Person.objects.create(**validated_data)
#     print(instance, 'dfdfdfs')
#     return instance

from rest_framework import serializers
from app2.models import *


class JonerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joner
        fields = ['name']
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name','release_date','joner','rating']


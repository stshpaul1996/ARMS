from rest_framework import serializers
from .models import *


class Visits(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
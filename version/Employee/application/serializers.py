from . models import Details
from rest_framework import serializers

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = "__all__"
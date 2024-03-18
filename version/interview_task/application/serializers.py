from .models import Detail
from rest_framework.serializers import ModelSerializer

class DetailSerializer(ModelSerializer):
    class Meta:
        model = Detail
        fields = "__all__"


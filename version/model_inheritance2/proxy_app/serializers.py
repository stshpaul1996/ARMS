from . models import Proxy_model
from rest_framework.serializers import ModelSerializer
class Proxy_modelSerializer(ModelSerializer):
    class Meta:
        model = Proxy_model
        fields = "__all__"
        
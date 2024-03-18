from . models import Proxy_model
from . serializers import Proxy_modelSerializer
from rest_framework import viewsets
# Create your views here.
class Proxy_viewset(viewsets.ModelViewSet):
    queryset = Proxy_model.objects.all()
    serializer_class = Proxy_modelSerializer


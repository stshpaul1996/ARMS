from . models import Details
from . serializers import DetailSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class DetailViewSet(ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailSerializer
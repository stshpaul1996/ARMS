
from rest_framework import viewsets

from app1.models import Person
from app1.serializers import PersonSerializer
class PersonViewset(viewsets.ViewSet):
    def post_method(self, request):
        pass

class PersonModelViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
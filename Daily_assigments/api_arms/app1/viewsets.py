
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
# from app1.file1 import ModelViewSet
from django.utils import timezone
timezone.now()

from app1.models import Person
from app1.serializers import PersonSerializer
class PersonViewset(viewsets.ViewSet):
    def post_method(self, request):
        pass

class PersonModelViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def create(self,request,*args, **kwargs):
        # super().create(self*args, **kwargs)
        print(request.user)
        print(request)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        serializer.validated_data['created_by'] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if not instance.status:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data["updated_date"] = timezone.now()
            serializer.validated_data["updated_by"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        else:
            msg = "No data found"
            return Response(msg,status = status.HTTP_404_NOT_FOUND)
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # import pdb; pdb.set_trace()
        msg = ''
        if not instance.status:
            instance.status = True
            instance.save()
            msg = "data deleted successfully"
            # return super().destroy(request, *args, **kwargs)
            return Response(msg,status = status.HTTP_404_NOT_FOUND)

        else :
            msg = "record not found"
            return Response(msg,status = status.HTTP_404_NOT_FOUND)

        # import pdb; pdb.set_trace()
        



        



























    
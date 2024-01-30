from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings

from app1.serializers import PersonSerializer

# class CreateModelMixin:
#     """
#     Create a model instance.
#     """
#     def create(self, request, *args, **kwargs):
#         serializer = PersonSerializer(data=request.data)
#         print(serializer)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#     def perform_create(self, serializer):
#         serializer.save()
#         serializer.created_by = self.request.user
#         serializer.save()



#     def get_success_headers(self, data):
#         try:
#             return {'Location': str(data[api_settings.URL_FIELD_NAME])}
#         except (TypeError, KeyError):
#             return {}





class CreateModel(mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        serializer = PersonSerializer(data=request.data)
        # print(seriali)
        serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        serializer.save()
        serializer.created_by = request.user
        serializer.save()
        print(request.user)
        print(serializer.data)

        # import pdb;pdb.set_trace()
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    # def perform_create(self, serializer):
    #     serializer.save()
    #     serializer.created_by_id = self.request.user
    #     serializer.save()


class ModelViewSet(CreateModel,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass

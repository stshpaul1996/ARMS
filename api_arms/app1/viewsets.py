
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import generics, mixins, views

from app1.models import Person, Role, MyUser
from app1.serializers import (PersonSerializer, UserSerializer,
                              RoleSerializer,
                              )

class RoleModelViewset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class PostAndPutViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin):
    pass

class PersonViewset(viewsets.ViewSet):
    def post_method(self, request):
        pass

class PersonModelViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# def USerPorfileSave(wrapper):
#     def inner_wrapper(*args, **kwargs):
#         UserProfile(user=kwargs.get("user"), role=kwargs.get("role")).save()
#         return wrapper(*args, **kwargs)
#     return inner_wrapper

class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
 
    # def perform_create(self, serializer):
    #     data = serializer.data
    #     #role_id = data.pop("role")
    #     user1 = User.objects.create_user(**data)
    #     # User.save()
    #     #role_inst = Role.objects.get(id=role_id)
    #     #UserProfile(user=user1, role=role_inst).save()
    #     #remove role from serializer.data
    #     # serializer.save()
    #     #add UserProfile

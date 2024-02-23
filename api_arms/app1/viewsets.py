
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import generics, mixins, views
from django.contrib.auth import get_user_model

from app1.models import Person, Role, MyUser, Api
from app1.serializers import (PersonSerializer, UserSerializer,
                              RoleSerializer, ApiSerializer
                              )
import logging 
logger = logging.getLogger(__name__)

class RoleModelViewset(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
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

class ApiModelViewset(viewsets.ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer

# def USerPorfileSave(wrapper):
#     def inner_wrapper(*args, **kwargs):
#         UserProfile(user=kwargs.get("user"), role=kwargs.get("role")).save()
#         return wrapper(*args, **kwargs)
#     return inner_wrapper

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
 
    def perform_create(self, serializer):
        logger.info("user creation started")
        data = serializer.data
        logger.debug(f"user {data.get('username')} creating")
        role_id = data.pop("role")
        role_inst = Role.objects.get(id=role_id)
        data['role'] = role_inst
        user1 = get_user_model().objects.create_user(**data)
        logger.info("user created")
        # role_inst = Role.objects.get(id=role_id)
        # user1.role = role_inst
        # user1.save()
        #UserProfile(user=user1, role=role_inst).save()
        #remove role from serializer.data
        # serializer.save()
        #add UserProfile

from permission_app.models import *
from permission_app.serializers import *
from rest_framework import viewsets


class RoleModelViewset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = Role_serializers
 
class PersonModelViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
 
class ApiModelViewset(viewsets.ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = Api_serializers
 
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = get_user_model().objects.all()
    serializer_class = MyUserSerializer
 
    def perform_create(self, serializer):
        data = serializer.data
        role_id = data.pop("role")
        role_inst = Role.objects.get(id=role_id)
        data['role'] = role_inst
        user1 = get_user_model().objects.create_user(**data)
        # role_inst = Role.objects.get(id=role_id)
        # user1.role = role_inst
        # user1.save()
        #UserProfile(user=user1, role=role_inst).save()
        #remove role from serializer.data
        # serializer.save()
        #add UserProfile
class PermissionModelViewset(viewsets.ModelViewSet):
    queryset=Permissions.objects.all()
    serializer_class=Permissions_serializers
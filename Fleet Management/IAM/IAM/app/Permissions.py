from rest_framework.permissions import BasePermission
from .models import  *
class CheckPermission(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        given_api = request.META["PATH_INFO"]
        role_inst = request.user.role
        api=Api.objects.get(name=given_api)
        permissons=Permissions.objects.get(role=role_inst,api=api)
        for  i in permissons:
            if request.method == 'GET':
                return i.has_get
            elif request.method == 'PUT':
                return i.has_put
            elif request.method == 'POST':
                return i.has_post
            elif request.method == 'PATCH':
                return i.has_patch
            elif request.method == 'DELETE':
                return i.has_delete

from django.contrib import admin
from permission_app.views import *
from permission_app.viewsets import *
from django.urls import path
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'user', UserViewSet, basename="user")
router.register(r'role', RoleModelViewset, basename='role')
router.register(r'api', ApiModelViewset, basename='api')
router.register(r'permission1', PermissionModelViewset, basename='permission')
router.register(r'person', PersonModelViewset, basename='viewset_person')
 
urlpatterns = [
   
 ] + router.urls
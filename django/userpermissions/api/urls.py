from django.contrib import admin
from django.urls import path
from api.views import RoleModelViewset,PersonModelViewset,ApiModelViewset,UserViewSet,PermissionsViewSet,LoginAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('role', RoleModelViewset, basename='role')
router.register('user', UserViewSet, basename='user')
router.register('api', ApiModelViewset, basename='api')
router.register('permissions', PermissionsViewSet, basename='permissions')
router.register('person', PersonModelViewset, basename='person')

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    
]+router.urls

from django.urls import path
from .views import LoginAPIView,UserProfileViewSet,RoleModelViewset,PermissionsModelViewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('user', UserProfileViewSet, basename="user")
router.register('role', RoleModelViewset, basename='role')
router.register('role', PermissionsModelViewset, basename='Permissions')

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
]+router.urls
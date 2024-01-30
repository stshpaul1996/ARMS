
from django.urls import path
from app1.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet, basename="user")
router.register(r'role', RoleViewset, basename="role")
router.register(r'permission', PermissionViewSet, basename="permission")
router.register(r'api', ApiViewSet, basename="api")

urlpatterns = [
    path("login/", LoginAPI.as_view()), 
]+router.urls

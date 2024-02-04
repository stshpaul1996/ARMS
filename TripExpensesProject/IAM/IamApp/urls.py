from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'user', MyUserView, basename="user")
router.register(r'role', RoleView, basename="role")
router.register(r'api', ApiView, basename="api")
router.register(r'permission', PermissionView, basename="permission")

urlpatterns = [
    path("login/", LoginAPIView.as_view())
 
]+router.urls
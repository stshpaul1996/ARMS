from .views import * 
from django.urls import path,include 
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


router.register(r'user', UserViewSet, basename="user")
router.register(r'role', RoleViewset, basename='role')
router.register(r'person',PersonModelViewset,basename = 'person')
router.register(r'api',ApiModelViewset,basename = 'api')
router.register(r'permissions',permissionViewset,basename='permission')
urlpatterns = [
   
    path("login/", LoginAPI.as_view()), 
] + router.urls

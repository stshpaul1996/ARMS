from django.urls import path
from app1.views import UserViewSet, RoleModelViewset, LoginAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet, basename="user")
router.register(r'role', RoleModelViewset, basename='role')



urlpatterns = [ 
    path("login/", LoginAPI.as_view()),
    
] + router.urls
from .views import * 
from django.urls import path,include 
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


router.register(r'user', MyuserViewset, basename="user")
router.register(r'role', RoleViewset, basename='role')

urlpatterns = [
   
    
] + router.urls

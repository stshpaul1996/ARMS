
from django.urls import path
from .viewsets import *
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


router.register(r'user', myUserViewset, basename="user")
router.register(r'phonenumber', userPhonenumberViewset, basename='phonenumber')
router.register(r'role',RoleViewswet,basename='role')

urlpatterns = [
    
    path("login",LoginApi.as_view()),
]+ router.urls

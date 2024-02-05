from django.urls import path
from . views import MyUserViewSet,RoleModelViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('user',MyUserViewSet,basename='user')
router.register('role',RoleModelViewSet,basename='role')
urlpatterns = [
]+router.urls
from django.urls import path
from . views import RoleModelVieset,UserProfileModelViewset
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("user",UserProfileModelViewset,basename="user")
router.register("role",RoleModelVieset,basename="role")
urlpatterns = [
]+router.urls
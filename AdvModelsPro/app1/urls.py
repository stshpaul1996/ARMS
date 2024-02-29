from django.urls import path
from .views import UserProfileView

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register(r'user', UserView, basename="user")
router.register(r'userprofile', UserProfileView, basename="userprofile")


urlpatterns = [
    
]+router.urls
from django.urls import path
from .views import ProxyViewsets
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('proxy', ProxyViewsets, basename="proxy")


urlpatterns = [
    
]+router.urls
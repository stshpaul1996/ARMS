from django.urls import path
from .views import EmpViewsets
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('employee', EmpViewsets, basename="employee")


urlpatterns = [
    
]+router.urls
from django.urls import path
from .views import StudentVeiwsets
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('student', StudentVeiwsets, basename="student")


urlpatterns = [
    
]+router.urls
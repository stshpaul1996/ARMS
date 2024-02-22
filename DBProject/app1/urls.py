from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'product', ProductView, basename='product')

urlpatterns = [
   
]+router.urls
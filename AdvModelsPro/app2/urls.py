from django.urls import path
from .views import ProxyView, VisitsView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'proxy', ProxyView, basename="proxy")
router.register(r'visit', VisitsView, basename="visit")



urlpatterns = [
    
]+router.urls
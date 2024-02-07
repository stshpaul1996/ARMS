from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, TripViewSet, AvailableVehiclesViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicles')
router.register(r'trips', TripViewSet, basename='trips')
router.register(r'available-vehicles', AvailableVehiclesViewSet, basename='available-vehicles')

urlpatterns = router.urls

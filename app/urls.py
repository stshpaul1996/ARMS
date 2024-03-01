from django.contrib import admin
from django.urls import path
from app.views import *
from app.viewsets import *
from rest_framework.routers import DefaultRouter 
router=DefaultRouter()
router.register(r'vehicle', VehicleViewSet, basename="vehicle")
router.register(r'trip', TripViewSet, basename="trip")

urlpatterns = [
    path("available/",AvailableVehicleAPIView.as_view())
    # path("available/<int:id>",AvailableVehicleAPIView.as_view())


] + router.urls


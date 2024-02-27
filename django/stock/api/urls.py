from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('customer', CustomerViewsets, basename="customer")
router.register('product', ProductViewsets, basename='productViewsets')
router.register('purchase', PurchaseViewsets, basename='purchase')
router.register('SalesViewsets', SalesViewsets, basename="SalesViewsets")
router.register('PurchaseorderViewsets', PurchaseorderViewsets, basename='PurchaseorderViewsets')
router.register('salesorderViewsets', salesorderViewsets, basename='salesorderViewsets')

urlpatterns = [
    
]+router.urls
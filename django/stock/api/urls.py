from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('customer', CustomerViewsets, basename="customer")
router.register('product', ProductViewsets, basename='productViewsets')
router.register('purchase', PurchaseViewsets, basename='purchase')
router.register('sales', SalesViewsets, basename="sales")
#router.register('purchaseorder', PurchaseorderViewsets, basename='purchaseorder')
router.register('salesorder', SalesorderViewsets, basename='salesorder')

urlpatterns = [
    path('purchaseorder/<int:id>',PurchaseorderViewsets.as_view())
    
]+router.urls
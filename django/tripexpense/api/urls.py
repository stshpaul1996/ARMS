from django.contrib import admin
from django.urls import path
from api.views import MemberViewSet,ExpenseViewSet,TripViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('member', MemberViewSet, basename='member'),
router.register('expense', ExpenseViewSet, basename='expense'),
router.register('trip', TripViewSet, basename='trip')


urlpatterns = [
    
]+router.urls

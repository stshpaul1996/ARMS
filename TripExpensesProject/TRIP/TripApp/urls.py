from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'trip', TripView, basename="trip")
router.register(r'member', MemberView, basename="member")
router.register(r'expense', ExpensesView, basename="expense")


urlpatterns = [
     #path("expense/", ExpensesView.as_view()) 
]+router.urls
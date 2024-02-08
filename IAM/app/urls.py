from django.contrib import admin
from app.views import *
from app.viewsets import *
from django.urls import path
from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'person', PersonViewSet, basename="person")
# router.register(r'user', MyUserViewSet, basename="user")
urlpatterns = [
    path("login/",Login.as_view())

 ] 


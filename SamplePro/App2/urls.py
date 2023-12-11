from django.urls import path
from .views import app_one

urlpatterns = [
    path("home/", app_one)
]

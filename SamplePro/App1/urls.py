from django.urls import path
from App1.views import app_one

urlpatterns = [
    path("home/", app_one)
]

from django.urls import path
from App3.views import app_one

urlpatterns = [
    path("app3/", app_one)
]

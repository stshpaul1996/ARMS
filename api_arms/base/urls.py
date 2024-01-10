from django.contrib import admin
from django.urls import path, include
from base.views import LoginAPI

urlpatterns = [

    path("login/", LoginAPI.as_view() )
]

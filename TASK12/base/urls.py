from django.contrib import admin
from django.urls import path
from base.views import base_customer_create_view

urlpatterns = [
    path('create/',base_customer_create_view)
]
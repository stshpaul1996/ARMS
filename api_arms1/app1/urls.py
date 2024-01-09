from django.contrib import admin
from django.urls import path, include
from app1.views import (ProductView, CategoryView)

urlpatterns = [
    path("product/", ProductView.as_view()),
    path("category/", CategoryView.as_view())
]
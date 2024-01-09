from django.contrib import admin
from django.urls import path, include
from app1.views import (SampleView, ProductView, CategoryView,PoductCostOpeningstockView)

urlpatterns = [
    # path("person/<int:pk>/", SampleView.as_view()),
    path("person/", SampleView.as_view()),
    path("product/", ProductView.as_view()),
    path("category/", CategoryView.as_view()),
    path("diff_data", PoductCostOpeningstockView.as_view()),

    
    
]

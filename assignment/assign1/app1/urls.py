from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns =[
    path('app1/',views.application1)
]
from django.contrib import admin
from django.urls import path
from app3.views import application3

urlpatterns =[
    path('app3/',application3)
]
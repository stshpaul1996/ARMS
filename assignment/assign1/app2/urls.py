from django.contrib import admin
from django.urls import path
from app2.views import application2

urlpatterns =[
    path('app2/',application2),
]
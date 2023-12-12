from django.contrib import admin
from django.urls import path
from sample.views import person1_create_view

urlpatterns = [
    path('person1/',person1_create_view)
]
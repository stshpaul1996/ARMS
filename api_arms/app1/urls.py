from django.contrib import admin
from django.urls import path, include
from app1.views import SampleView

urlpatterns = [
    path("<int:id>/", SampleView.as_view()),
    path("", SampleView.as_view()),
    
]

from django.contrib import admin
from django.urls import path, include
from app1.views import SampleView

urlpatterns = [
    # path("person/<int:pk>/", SampleView.as_view()),
    path("person/", SampleView.as_view()),
    
    
]

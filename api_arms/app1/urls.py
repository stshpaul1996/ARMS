from django.urls import path, include
from app1.views import SampleView

urlpatterns = [
    
    path('',SampleView.as_view()),
]

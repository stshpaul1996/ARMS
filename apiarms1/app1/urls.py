from django.urls import path
from app1.views import *
urlpatterns = [
    path("",SampleView.as_view()),
    path("student/",StudentView.as_view())
]

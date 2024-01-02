from django.urls import path
from app.views import *
urlpatterns = [
    path("",SampleView.as_view())
]

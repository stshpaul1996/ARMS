from django.urls import path
from app3.views import app3_show

urlpatterns = [
    path('', app3_show),
]

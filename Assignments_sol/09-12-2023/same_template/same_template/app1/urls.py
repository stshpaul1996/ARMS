from django.urls import path
from .views import app1_show

urlpatterns = [
    path('', app1_show),
]

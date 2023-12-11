from django.urls import path
from .views import app2_show

urlpatterns = [
    path('', app2_show),
]

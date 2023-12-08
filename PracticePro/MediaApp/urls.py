from django.urls import path

from .views import media_view

urlpatterns = [
    path("", media_view),
    
]

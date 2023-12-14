from django.urls import path
from app4.views import Tourist_view


urlpatterns = [
    path("",Tourist_view)
]

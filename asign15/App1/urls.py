
from django.urls import path
from .views import entrepreneur_details_view

urlpatterns = [
    path("abc", entrepreneur_details_view),
]

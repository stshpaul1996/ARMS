from django.urls import path
from .views import home_view, details_view

urlpatterns = [
    path("", home_view),
    path("<str:name>/", details_view)
    
]

from django.urls import path
from . import views
urlpatterns = [
    path("", views.adding),
    path("dis/", views.display)
]
from django.urls import path
from . import views
urlpatterns = [
    path("", views.uploading),
    path("lists/", views.listing),
]
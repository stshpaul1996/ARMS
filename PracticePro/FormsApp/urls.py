from django.urls import path

from .views import form_view, register_view

urlpatterns = [
    path("", form_view),
    path("data/", register_view)
]
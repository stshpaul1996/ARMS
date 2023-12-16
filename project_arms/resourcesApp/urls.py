from django.urls import path

from .views import resources_view, form_view, users_view

urlpatterns = [
    path("", resources_view),
    path("register/", form_view),
    path("registered_candidates/", users_view)

]
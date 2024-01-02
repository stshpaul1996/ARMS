from django.urls import path
from app.views import user_view

urlpatterns = [
    path("users/",user_view)
]

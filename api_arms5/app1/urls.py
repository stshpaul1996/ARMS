from django.urls import path
from app1.views import login_view

urlpatterns = [
    path('auth/',login_view.as_view())
]

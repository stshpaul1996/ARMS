from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.LoginAPIView.as_view(),name="api")
]

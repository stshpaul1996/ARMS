from django.urls import path
from .views import*

urlpatterns = [
   path('token/', Login_api.as_view()),
]
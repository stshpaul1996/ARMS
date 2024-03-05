from django.urls import path
from .views import IAM

urlpatterns = [
    path('token/',IAM.as_view()),
]

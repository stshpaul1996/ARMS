from django.urls import path
from .views import*

urlpatterns = [
   path('', Login_api.as_view()),
]
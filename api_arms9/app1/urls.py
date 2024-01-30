from django.urls import path
from .views import*

urlpatterns = [
   path('auth/', Personv.as_view()),
]
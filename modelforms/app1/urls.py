from django.urls import path
from app1 import views

urlpatterns = [
  
    path('upload/',views.asp),
    path('view/',views.see),
]
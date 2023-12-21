from django.urls import path,include
from app1 import views

urlpatterns = [
    path('upload/',views.Upload),
    path('home/',views.home),
]

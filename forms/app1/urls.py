from django.urls import path
from app1 import views

urlpatterns = [
    path('upload/',views.asp),
    path('<str:name1>/',views.see)
]

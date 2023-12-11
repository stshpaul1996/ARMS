from django.urls import path
from third_app import views

urlpatterns=[
    path('login/',views.login),
]
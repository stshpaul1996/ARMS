
from django.urls import path
from .views import Person_detail

urlpatterns = [
    path('<str:name>/', Person_detail, name='Person_detail'),
]
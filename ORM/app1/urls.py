from django.urls import path
from .views import *

urlpatterns = [
    path('orm/', VisitV.as_view()),
]
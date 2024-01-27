from django.urls import path
from .views import*

urlpatterns = [
   path('auth1/', Personv.as_view()),
]
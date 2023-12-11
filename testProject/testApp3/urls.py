from django.urls import path
from testApp3 import views
urlpatterns = [
    path('testapp3/', views.app3),
]
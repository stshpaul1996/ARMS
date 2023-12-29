from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page),
    path('add/',views.add_aspirant),
    path('dis/',views.display),
]
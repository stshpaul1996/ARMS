from django.urls import path
from . import views
urlpatterns = [
    path('movie/',views.movie),
    path("<str:name>/",views.displays),
]
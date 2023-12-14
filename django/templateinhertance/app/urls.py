from django.contrib import admin
from django.urls import path,include
from .constants import player_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:name>/',player_view)
]
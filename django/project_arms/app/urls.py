from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aspirant/',views.add_aspirant_view),
    path('aspirantget/',views.get_aspirant_view)
]
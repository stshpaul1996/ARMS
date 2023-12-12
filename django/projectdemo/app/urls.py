from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home_view),
    path('about/',views.about),
    path('contactus/',views.contactus),
    path('feedback/',views.feedback),
]
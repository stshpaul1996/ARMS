from django.contrib import admin
from django.urls import path
from app.views import SampleView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',SampleView.as_view()),
    path('put/<int:pk>/',SampleView.as_view()),
    path('delete/<int:pk>/',SampleView.as_view()),
]
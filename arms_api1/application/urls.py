from django.urls import path
from . import views

urlpatterns = [
    path('employee/',views.EmployeeAPIView.as_view()),
    path('employee/<int:pk>/',views.EmployeeAPIView.as_view()),
    path('department/',views.DepartmentAPIView.as_view()),
    path('department/<int:pk>/',views.DepartmentAPIView.as_view()),
]

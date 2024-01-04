from django.urls import path, include
from app1.views import SampleView, Employees, Departments

urlpatterns = [

    path('',SampleView.as_view()),
    path('emp/',Employees.as_view()),
    path('dep/',Departments.as_view()),
]

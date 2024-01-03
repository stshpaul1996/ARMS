from django.urls import path
from . import views

urlpatterns = [
    path('sam/',views.SampleView.as_view()),
    path('dept/',views.DepartmentView.as_view()),
    path('dept/<int:pk>/',views.DepartmentView.as_view()),
    path('emp/',views.EmployeeView.as_view()),
    path('emp/<int:pk>/',views.EmployeeView.as_view()),
]
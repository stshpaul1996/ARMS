from django.urls import path
from .views import EmployeeView, DepartmentView
urlpatterns = [
    path("", EmployeeView.as_view()),
    path("<int:id>/", EmployeeView.as_view()),
    path("dep/", DepartmentView.as_view()),
    path("dep/<int:id>/", DepartmentView.as_view()),

    
]

from django.urls import path
from . views import SampleView,EmployeeView
urlpatterns = [
    path("emp/", EmployeeView.as_view()),
    path("<int:id>/",SampleView.as_view()),
    path("sam/",SampleView.as_view()),
    
]
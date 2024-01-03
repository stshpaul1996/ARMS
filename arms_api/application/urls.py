from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('sam/',views.SampleView.as_view()),
    path('dept/',views.DepartmentView.as_view()),
    path('dept/<int:pk>/',views.DepartmentView.as_view()),
    path('emp/',views.EmployeeView.as_view()),
    path('emp/<int:pk>/',views.EmployeeView.as_view()),
=======
from . views import SampleView,EmployeeView
urlpatterns = [
    path("emp/", EmployeeView.as_view()),
    path("<int:id>/",SampleView.as_view()),
    path("sam/",SampleView.as_view()),
    
>>>>>>> 7cddd1a6d8b4c25cbb443e8281aa1a3452c5f16a
]
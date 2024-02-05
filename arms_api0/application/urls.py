from django.urls import path
from . import views
urlpatterns = [
    path('',views.SampleView.as_view()),
    path('stu/<int:pk>/',views.StudentView.as_view()),
    path('stu/',views.StudentView.as_view()),
]
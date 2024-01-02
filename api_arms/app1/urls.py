
from django.urls import path
from .views import employee_view,department_view


urlpatterns = [
    path("emp/<int:id>",employee_view.as_view()),
    path("emp/",employee_view.as_view()),
    #path("emp/<int:id>",employee_view.as_view()),
    path("dept/",department_view.as_view()),
    path("dept/<int:id>",department_view.as_view()),
]
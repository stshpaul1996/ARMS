from django.urls import path
from modelApp.views import home_view,employee_view,models_view,daily_attendance_view,attendance_details_view,technology_view,technology_details_view,emp_tech_db_view,emp_tech_view

urlpatterns = [
    path("",home_view),
    path("emp",employee_view),
    path("db",models_view),
    path("attendance",daily_attendance_view),
    path("attendancedb",attendance_details_view),
    path("technology",technology_view),
    path("technologydb",technology_details_view),
    path("emptech",emp_tech_view),
    path("emptechdb",emp_tech_db_view)
]

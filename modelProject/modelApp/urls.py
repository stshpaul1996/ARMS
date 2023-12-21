
from django.urls import path
from modelApp.views import employee_view,models_view,daily_attendance_view,attendance_details_view

urlpatterns = [
    
    path("",employee_view),
    path("db",models_view),
    path("attendance",daily_attendance_view),
    path("attendancedb",attendance_details_view)
]

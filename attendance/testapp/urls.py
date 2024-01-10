from django.urls import path,include

from testapp.views import emp_form,emp_details_view,attendace_form,attendace_details_view


urlpatterns = [
    
    path('emp',emp_form),
    path('emp_details',emp_details_view),
     path('attendance',attendace_form),
      path('attendance_details',attendace_details_view),
        # path('delete/<str:id>',delete_row)


]

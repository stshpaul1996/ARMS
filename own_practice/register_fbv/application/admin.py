from django.contrib import admin
from . models import Aspirant
# Register your models here.

@admin.register(Aspirant)
class AspirantAdmin(admin.ModelAdmin):
    list_display=["F_name","L_name","Email_id","Phone_no","Graduation","Graduation_Stream","Graduation_Passed_Out_Year","Post_Graduation","Post_Graduation_Stream","Post_Gradation_Passed_out_year","Trained_on_Technology","Where_did_you_trained_Institute_Name","Duration_of_Course","Reference_Name","Where_did_you_hear_about_the_interview","Experience","Previous_Company_Name","Current_CTC","Expected_CTC","Do_you_Have_PF_in_last_company","How_Many_years_of_Experience","created_at"]
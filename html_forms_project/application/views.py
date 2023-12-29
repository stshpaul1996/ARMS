from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from . models import Aspirant
# Create your views here.
def home_page(request):
    return render(request,"application/base.html")

def add_aspirant(request):
    errors={}
    if request.method == 'POST':
        data=request.POST
        a=Aspirant(F_name=data["F_name"],
                   L_name=data["L_name"],
                   Email_id=data["Email_id"],
                   Phone_no=data["Phone_no"],
                   Graduation=data["Graduation"],
                   Graduation_Stream=data["Graduation_Stream"],
                   Graduation_Passed_Out_Year=data["Graduation_Passed_Out_Year"],
                   Post_Graduation=data["Post_Graduation"],
                   Post_Graduation_Stream=data["Post_Graduation_Stream"],
                   Post_Gradation_Passed_out_year=data["Post_Gradation_Passed_out_year"],
                   Trained_on_Technology=data["Trained_on_Technology"],
                   Where_did_you_trained_Institute_Name=data["Where_did_you_trained_Institute_Name"],
                   Duration_of_Course=data["Duration_of_Course"],
                   Reference_Name=data["Reference_Name"],
                   Where_did_you_hear_about_the_interview=data["Where_did_you_hear_about_the_interview"],
                   Experience=data["Experience"],
                   Previous_Company_Name=data["Previous_Company_Name"],
                   Current_CTC=data["Current_CTC"],
                   Expected_CTC=data["Expected_CTC"],
                   Do_you_Have_PF_in_last_company=data["Do_you_Have_PF_in_last_company"],
                   How_Many_years_of_Experience=data["How_Many_years_of_Experience"]
        )
        try:
            a.full_clean()
        except ValidationError as e:
            errors=e.message_dict
        if not errors:
            a.save()
            return redirect("display")
    return render(request,"application/add.html",{"errors":errors})

def display(request):
    d=Aspirant.objects.all()
    return render(request,"application/display.html",{"d":d})
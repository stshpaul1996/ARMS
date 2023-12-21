from django.shortcuts import render,redirect

# Create your views here.

from .forms import EmployeeForm,DailyAttendanceForm
from .models import Employee,Daily_Atendance
def employee_view(request):
    form  = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee_details = Employee(email_id = form.cleaned_data['email_id'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name = form.cleaned_data['last_name'],
                                        validate_phone_number = form.cleaned_data['validate_phone_number'],
                                        address = form.cleaned_data['address'],
                                        tech_id = form.cleaned_data['tech_id']
                                        )
            employee_details.save()
            return redirect("/app1/db")
               
    return render(request,'app1/employee_details.html',{'form':form})

def models_view(request):
    data = Employee.objects.all()
    if data:
        return render(request,"app1/db.html",{"data":data})
    
def daily_attendance_view(request):
    form  = DailyAttendanceForm()

    if request.method == "POST":
        form = DailyAttendanceForm(request.POST)
        if form.is_valid():
            details = Daily_Atendance(employee_id = form.cleaned_data['employee_id'],
                                      date = form.cleaned_data['date'],
                                      check_in = form.cleaned_data['check_in'],
                                      check_out = form.cleaned_data['check_out'],
                                      status = form.cleaned_data['status'])
            details.save()
            return redirect("/app1/attendance")
    return render(request,"app1/attendance_details_form.html",{'form':form})

def attendance_details_view(request):
    data = Daily_Atendance.objects.all()
    if data:
        return render(request,"/app1/attendance_details_db.html/",{"data":data})
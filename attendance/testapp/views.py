from django.shortcuts import render,redirect
from testapp.forms import Employee_Form,Daily_Atendance_form
from testapp.models import Employee,Daily_Atendance
from django.http import HttpResponse
# Create your views here.

def emp_form(request):
    c = Employee_Form()
    if request.method == 'POST':
        c = Employee_Form(request.POST)
        if c.is_valid():
            data = Employee(   email_id = c.cleaned_data['email_id'],first_name =  c.cleaned_data['first_name'],
                               last_name = c.cleaned_data['last_name'],
                                validate_phone_number = c.cleaned_data['validate_phone_number'],
                                address = c.cleaned_data['address'],
                                 tech_id =c.cleaned_data['tech_id'],)
            data.save()
            return redirect('/emp_details')
        
    return render(request,'testapp/emp.html',{'form':c})

def emp_details_view(request):
    data = Employee.objects.all()
    return render(request,'testapp/emp_details.html',{'data':data})


def attendace_form(request):
    c = Daily_Atendance_form()
    if request.method == 'POST':
        c = Daily_Atendance_form(request.POST)
        if c.is_valid():
            data = Daily_Atendance(  


                employee_id = c.cleaned_data['employee_id'],
               date = c.cleaned_data['date'],
              check_in = c.cleaned_data['check_in'],
             check_out =c.cleaned_data['check_out'],
             status = c.cleaned_data['status']
                
                
                
            )
            data.save()
            return redirect('/attendance_details')
        
    return render(request,'testapp/attendanceForm.html',{'form':c})


        

def attendace_details_view(request):
    data = Daily_Atendance.objects.all()
    return render(request,'testapp/attendanceView.html',{'data':data})


# def delete_row(request,id):
#     print(id)
#     return HttpResponse(id)

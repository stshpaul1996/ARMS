from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from .models import Employee ,Pricipal_consultant,Employee_exit,Deployed
from .forms import EmployeeForm ,PricipalContentForm,ExitForm,DeployedForm
def register_employee(request):
    if request.method == 'POST':
        eform = EmployeeForm(request.POST)
        if eform.is_valid():
            eform.save()
            messages.success(request, 'Form submitted successfully!')
            data = Employee.objects.all()
            return render(request, 'employee.html', {'data': data})
        else :
            messages.success(request, 'Form  not submitted ')
            return render(request,'register_employee.html',{'form':eform})
    else:
        eform =EmployeeForm()
        return render(request,'register_employee.html',{'form':eform})

def register_principal_consultant(request):
    if request.method == 'POST':
        eform = PricipalContentForm(request.POST)
        if eform.is_valid():
            eform.save()
            messages.success(request, 'Form submitted successfully!')
            return HttpResponseRedirect('/')
        else :
            messages.success(request, 'Form  not submitted ')
            return render(request,'register_Pricipal_consultant.html',{'form':eform})
    else:
        eform =PricipalContentForm()
        return render(request,'register_Pricipal_consultant.html',{'form':eform})

def register_Employee_exit(request):
    if request.method == 'POST':
        eform = ExitForm(request.POST)
        if eform.is_valid():
            eform.save()
            messages.success(request, 'Form submitted successfully!')
            data = Employee_exit.objects.all()
            return render(request, 'exit.html', {'data': data})
        else :
            messages.success(request, 'Form  not submitted ')
            return render(request,'register_employee_exit.html',{'form':eform})
    else:
        eform =ExitForm()
        return render(request,'register_employee_exit.html',{'form':eform})

def register_Deployed(request):
    if request.method == 'POST':
        eform = DeployedForm(request.POST)
        if eform.is_valid():
            eform.save()
            messages.success(request, 'Form submitted successfully!')
            return HttpResponseRedirect('/')
        else :
            messages.success(request, 'Form  not submitted ')
            return render(request,'register_deployed.html',{'form':eform})
    else:
        eform =DeployedForm()
        return render(request,'register_deployed.html',{'form':eform})



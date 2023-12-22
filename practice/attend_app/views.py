from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import EmployeeInfo,Daily_attendance
from .forms import EmployeeModelForm

# def add_employee(request):
#     if request.method=='POST':
#         data=request.POST
#         Employee(employee_id=data['employeee_id'], first_name=data['first_name'],
#                  last_name=data['last_name'],email=data['email'],date_of_join=data['date_of_join'],
#                  technology_id=data['technology_id'],mobile_no=data['mobile_no']).save()
#         return HttpResponse("employee submitted successfully")
#     else:
#         return render(request,"emp.html")
    
def empdetail(request):
    res=EmployeeInfo.objects.all()
    return render(request,"empdeta.html",{"res":res})




# def attend(request):
#     if request.method=='POST':
#         data=request.POST
#         Daily_attendance(employee_id=data['employee_id'],date=data['date'],
#                          login_time=data['login_time'],logout_time=data['logout_time'],status=data['status']).save()
#         return HttpResponse('form submitted successfully')
#     else:
#         return render(request,'attend.html')

def empdata(request):
    if request.method=='POST':
        form=EmployeeModelForm(data = request.POST,files = request.FILES)
        if form.is_valid():
            # empid = form.cleaned_data('employee_id')
            # firstName=form.cleaned_data('first_name')
            # lastName=form.cleaned_data('last_name')
            # Email=form.cleaned_data('email')
            # dateofjoin=form.cleaned_data('date_of_join')
            # technology=form.cleaned_data('technology_id')
            # mobile=form.changed_data('mobile_no')
            # data=EmployeeInfo(employee_id=empid,first_name=firstName,last_name=lastName,email=Email,date_of_join=dateofjoin,technology_id=technology,mobile_no=mobile)
            # data.save()
          form.save()
          return redirect('ed/')

        return HttpResponse('employee data saved successfully')
    else:
        form=EmployeeModelForm()
        return render(request,'emp.html',{'form':form})





   



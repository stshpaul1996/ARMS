from django.shortcuts import render
from django.http import HttpResponse
from app1.models import aspirant

# Create your views here.
def asp(request):
    if request.method == 'POST':
        data = request.POST
        aspirant_inst = aspirant(first_name=data['First Name'],
                                 last_name=data['Last Name/Surname'],
                                 email_ID=data['Email'],
                                 phone_No=data['Phone Number'],
                                 graduation=data['Graduation'],
                                 stream=data['Graduation Stream'],
                                 grad_yop=data['Graduation Passed out year'],
                                 post_graduation=data['Post Graduation'],
                                 Pg_Stream=data['Post Graduation Stream'],
                                 Pg_Passed_Out_Year=data['Post Graduation Graduation Passed out year'],
                                 Trained_On_Technology=data['Trained On Technology'],
                                 Institute_Name=data['Institute Name'],
                                 Duration_of_course=data['Duration of course'],
                                 Reference_Name=data['Reference Name'],
                                 hear_about_the_interview=data['Where did you heard about the interview'],
                                 Experience=data['Experience'],
                                 Previous_company_Name=data['Previous company Name'],
                                 Current_CTC=data['Current CTC'],
                                 Expected_CTC=data['Expected CTC'],
                                 PF_in_Last_Company=data['PF in Last Company'],
                                 )
        aspirant_inst.save()
        message = 'The upload is sucessfull'
    else:
        message = 'Unsucessfull'
    return render(request,'app1/forms.html',{'message':message})
                                 


def see(request,name1):
    data = aspirant.objects.all()
    for i in data:
        if i.first_name == name1:
            
            return render(request,'app1/index.html',{'data1':data,'var':i})
    else:
        return HttpResponse(name1)



from django.shortcuts import render
from .models import Aspirant,Rounds,Onboared
# Create your views here.
def aspirant_view(request):
    message=''
    if request.method=='POST':
        data=request.POST
        obj=Aspirant(full_name=data['full_name'],
                     email=data['email'],phone_no=data['phone_no'],gradution=data['gradution'],
                     post_gradution=data['post_gradution'],stream=data['stream'],passed_out_year=data['passed_out_year'],
                     trained_on_technology=data['trained_on_technology'],trained_institue=data['trained_institue'],
                     duration_of_course=data['duration_of_course'],reference_name=data['reference_name'],
                     hear_about_interview=data['hear_about_interview'],experience=data['experience'],
                     Previous_company_name=data['Previous_company_name'],current_ctc=data['current_ctc'],expected_ctc=data['expected_ctc'],
                     last_company=data['last_company'],years_of_experience=data['years_of_experience'],created_at=data['created_at'])
        
        obj.save()
        message='application created successful.'     
    else:
        message=''
    return render(request,'aspirant.html',{'message':message})
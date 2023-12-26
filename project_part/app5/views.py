from django.shortcuts import render
from app5.models import Users,Rounds,Joined
from django.http import HttpResponse

# Create your views here.
##by using forms
def users_view(request):
    if request.method=="POST":
        data=request.POST
        b = Users(first_name=data['first_name'],last_name=data['last_name'],email_id=data['email_id'],phone_no=data['phone_no'],
                            graduation=data['graduation'],graduation_stream=data['graduation_stream'],graduation_year=data['graduation_year'],post_graduation=data['post_graduation'],
                            post_graduation_stream=data['post_graduation_stream'],post_graduation_year=data['post_graduation_year'],trained_on_technology=data['trained_on_technology'],institute_name=data['institute_name'],
                            course_duration=data['course_duration'],reference_name=data['reference_name'],experience=data['experience'],
                            experience_years=data['experience_years'],previous_company_name=data['previous_company_name'],current_ctc=data['current_ctc'],expected_ctc=data['expected_ctc'],
                            pf=data['pf'])
        b.save()
        return HttpResponse("You have successfully registered")
    else:
        return render(request, "app5/users.html")
    
def registered(request):
        result=Users.objects.all()
        return render(request, "app5/home.html" , {"result":result})



def rounds_view(request):
    if request.method=="POST":
        inf=request.POST
        # user_id = Users.objects.get(id=id)
        c = Rounds(online_marks=inf['online_marks'],online_status=inf['online_status'],online_feedback=inf['online_feedback'],
                 tech_marks=inf['tech_marks'],tech_status=inf['tech_status'],tech_feedback=inf['tech_feedback'],
                 comm_marks=inf['comm_marks'],comm_status=inf['comm_status'],comm_feedback=inf['comm_feedback'], 
                 is_selected=inf['is_selected'])
        c.save()
        return HttpResponse("success")
        # res1=Rounds.objects.all()
        # return render(request, "app5/rounds.html", {"res1":res1})
    else:
        return render(request, "app5/rounds.html")
    
def roundscomple(request):
        res1=Rounds.objects.all()
        return render(request, "app5/home1.html", {"res1":res1})
    
def join_view(request,id):
    if request.method=="POST":
        # user_id = Users.objects.get(id=id)
        d=Joined(is_joined=data1['is_joined'],user_id=data1['user_id'])
        d.save()
        res2=Joined.objects.all()
        return render(request,"app5/join.html",{"res2":res2})
    else:
        return HttpResponse("check")


##by using modelforms
from app5.forms import Usersform,Roundsform,Joinedform
def userview(request):
    print(request.method, 'methodddddddd')
    if request.method=="POST":
              print(request.POST, 'posttttttttt')
              form=Usersform(request.POST)
              if form.is_valid():
                   form.save()
                   form = Usersform
    else:
          form=Usersform

    return render(request, "app5/userform.html", {"form":form})              
def roundview(request):
    print(request.method, 'methodddddddd')
    if request.method=="POST":
              print(request.POST, 'posttttttttt')
              form=Roundsform(request.POST)
              if form.is_valid():
                   form.save()
                   form = Roundsform
    else:
          form=Roundsform

    return render(request, "app5/roundform.html", {"form":form})      
def joinview(request):
    print(request.method, 'methodddddddd')
    if request.method=="POST":
              print(request.POST, 'posttttttttt')
              form=Joinedform(request.POST)
              if form.is_valid():
                   form.save()
                   form = Joinedform
    else:
          form=Joinedform

    return render(request, "app5/roundform.html", {"form":form})   
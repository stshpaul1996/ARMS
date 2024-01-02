from django.shortcuts import render,redirect
from app5.models import Users,Rounds,Joined
from django.http import HttpResponse
from .forms import Usersform

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
        return render(request, "app5/1home.html" , {"result":result})



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
        return render(request, "app5/2home1.html", {"res1":res1})
    
def join_view(request):
    if request.method=="POST":
        # user_id = Users.objects.get(id=id)
        # d=Joined(is_joined=data1['is_joined'],user_id=data1['user_id'])
        # d.save()
        res2=Joined.objects.all()
        return render(request,"app5/join.html",{"res2":res2})
    else:
        return HttpResponse("check")


def  joincomple(request):
       data=Joined.objects.all()
       return render(request, "app5/3joins.html", {"data":data})


##by using modelforms
from app5.forms import Usersform,Roundsform,Joinedform
def userview(request):
    if request.method=="POST":
              form=Usersform(request.POST)
              if form.is_valid():
                   form.save()
                   form = Usersform
    else:
          form=Usersform

    return render(request, "app5/userform.html", {"form":form})              
def roundview(request):
    if request.method=="POST":
              form=Roundsform(request.POST)
              if form.is_valid():
                   form.save()
                   form = Roundsform
    else:
          form=Roundsform

    return render(request, "app5/roundform.html", {"form":form})      
def joinview(request):
    if request.method=="POST":
              form=Joinedform(request.POST)
              if form.is_valid():
                   form.save()
                   form = Joinedform
    else:
          form=Joinedform

    return render(request, "app5/joinedform.html", {"form":form})   


def base(request):
      return render(request,"app5/navbar.html")

# def update_view(request,id):
#        data=Users.objects.get(id=id)
#        if request.method == 'POST':
#              form=Usersform(instance=data)
#              if form.is_valid():
#                 print("kkkkkkkkkk")
#                 form=Usersform(request.POST, instance=data)
#                 form.save()
#                 return render(request,"app5/success.html") 
#        return render(request,"app5/update_userform.html", {"form":form})      
      

def update_view(request, id):
    data = Users.objects.get(id=id)
    if request.method == 'POST':
        form = Usersform(request.POST, instance=data)
        if form.is_valid():
            print("kkkkkkkkkk")
            form.save()
            return render(request, 'app5/success.html')  # Replace with your success URL name
    else:
        form = Usersform(instance=data)

    return render(request, 'app5/update_userform.html', {'form': form})
def delete_view(request,id):
     res=Users.objects.get(id=id)
     res.delete()
     return redirect("after_delete_registered")
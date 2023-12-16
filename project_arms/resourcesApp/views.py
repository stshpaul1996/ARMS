from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Resources

# Create your views here.
def resources_view(request):
    return render(request,"resources/header.html")

def form_view(request):
    if request.method == 'GET':
        return render(request, "resources/register.html")
    else:
        post = request.POST
        Resources(
            first_name = post.get('first'),
            last_name = post.get('last'),
            email = post.get('email'),
            phone = post.get('phone'),
            graduation = post.get('grad'),
            stream = post.get('stream'),
            year = post.get('year'),
            pg = post.get('pg'),
            pg_stream = post.get('pgstream'),
            pg_year = post.get('pgyear'),
            trained_technology = post.get('trainedtech'),
            institute_name = post.get('institutename'),
            duration_course = post.get('duration'),
            reference_name = post.get('reference'),
            hear_interview = post.get('hear'),
            work_experience = post.get('work'),
            years_experience = post.get('experience'),
            company_name = post.get('company'),
            current_ctc = post.get('current'),
            expected_ctc = post.get('expected'),
            pf = post.get('pf'), 
        ).save()
        return render(request, "resources/success.html")
       



    

def users_view(request):
    db_data = Resources.objects.all()
    return render(request, "resources/users.html", {"content":db_data})
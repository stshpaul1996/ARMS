from django.shortcuts import render,redirect
from . forms import Aspirant_form,SignUpForm
from . models import Aspirant
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request,"application/base.html")

def adding(request):
    form=Aspirant_form()
    if request.method == 'POST':
        form=Aspirant_form(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            experience=form.cleaned_data["Experience"]
            if experience.lower()=="no":
                data.Previous_Company_Name=None
                data.Current_CTC=None
                data.Expected_CTC=None
                data.Do_you_Have_PF_in_last_company=None
                data.How_Many_years_of_Experience=None
            data.save()
            return redirect("thank")
        else:
            print("some validations are wrong")
    return render(request,"application/aspirant.html",{"form":form})


@login_required
def display(request):
    d=Aspirant.objects.all()
    return render(request,"application/display.html",{"d":d})

def thank(request):
    return render(request,"application/thanks.html")

def signup_view(request):
    form = SignUpForm()
    if request.method == "POST":
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return redirect("/accounts/login") 
    return render(request,"application/signup.html",{"form":form})

def logout_view(request):
    logout(request)
    return render(request,"application/logout.html")
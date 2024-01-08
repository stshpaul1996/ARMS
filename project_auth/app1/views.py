from django.shortcuts import render, redirect
from app1.models import Person
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect("/")

def login_view(request):
    if request.method=="POST":
        data = request.POST
        user = authenticate(username=data.get("username"), password=data.get("password"))
        if user:
            login(request, user)
            return redirect("/")
    return render(request, "login.html")
def base_view(request):
    return render(request, "base.html")


@login_required
def person_view_create(request):
    if request.method == "POST":
        per = Person(name=request.POST.get("name"))
        per.save()
    
    return render(request, "index.html")

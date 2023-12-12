from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"app1/home.html")

def nithisha_view(request):
    return render(request,"app1/nithisha.html")

def kalkuri_view(request):
    return render(request,"app1/sai.html")

def parasa_view(request):
    return render(request,"app1/lakshmi.html")


def kspaul_view(request):
    return render(request,"app1/satish.html")


def haritha_view(request):
    return render(request,"app1/haritha.html")
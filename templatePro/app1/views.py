from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "app1/home.html")

def tech_view(request):
    return render(request, "app1/tech.html")

def science_view(request):
    return render(request, "app1/science.html") 

def health_view(request):
    return render(request,"app1/health.html")

def business_view(request):
    return render(request, "app1/business.html")
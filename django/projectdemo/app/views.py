from django.shortcuts import render


# Create your views here.
def home_view(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contactus.html')

def feedback(request):
    return render(request,'feedback.html')
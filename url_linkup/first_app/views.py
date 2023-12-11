from django.shortcuts import render

def home(request):
    return render(request,'app1/a.html')

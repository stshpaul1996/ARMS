from django.shortcuts import render

# Create your views here.
def display1(request):
    return render(request,'temp1.html')
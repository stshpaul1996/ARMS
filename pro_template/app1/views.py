from django.shortcuts import render

def home_view(request):
    return render(request,'home.html')

def kalam(request):
    return render(request,'kalam.html')

def singh(request):
    return render(request,'singh.html')

def shivaji(request):
    return render(request,'shivaji.html')

def ashoka(request):
    return render(request,'ashoka.html')

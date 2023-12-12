from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'app1/home.html')
def Prime(request):
    return render(request,'app1/prime.html')
def Bumblebee(request):
    return render(request,'app1/bumblebee.html')
def Megatron(request):
    return render(request,'app1/megatron.html')
def Grimlock(request):
    return render(request,'app1/grimlock.html')
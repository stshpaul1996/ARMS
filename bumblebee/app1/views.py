from django.shortcuts import render
from .constants import data_prime

# Create your views here.
def home_view(request):
    return render(request,'app1/home.html')
def Prime(request):
    context ={'data1':data_prime}
    return render(request,'app1/prime.html',context)
def Bumblebee(request):
    context ={'data1':data_prime}
    return render(request,'app1/bumblebee.html',context)
def Megatron(request):
    return render(request,'app1/megatron.html')
def Grimlock(request):
    return render(request,'app1/grimlock.html')
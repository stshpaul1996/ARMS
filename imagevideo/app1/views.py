from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CricketerModelForm
from .models import Cricketer


# Create your views here.
def Upload(request):
    message =''
    form = CricketerModelForm()
    if request.method == 'POST':
        form = CricketerModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = CricketerModelForm()
            message ='The upload is sucessful'
            return redirect('home')
        else:
            message ='The upload is unsucessful'
    else:
        message='The upload is unsucessful'
    return render(request, 'app1/upload.html',{'form':form, 'message':message})

def home(request):
    data = Cricketer.objects.all()
    return render(request,'app1/home.html',{'data1':data})
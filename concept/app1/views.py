from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Aspirant
from app1.forms import AspirantModelForm, RoundComForm,RoundTechForm,RoundCEOForm,OnboaredForm
from django.shortcuts import redirect

# Create your views here.
def Home(request):
    message = ''
    if request.method == 'POST':
        data = request.POST
        message = 'The upload is sucessfull'
        form = AspirantModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = AspirantModelForm()
            return redirect('list')
        else:
            message ='The upload is not sucessfull'
    else:
        form = AspirantModelForm()
        message = 'The upload is not sucessfull'
    return render(request,'app1/Home.html',{'message':message,'form':form})
                                 


def List(request):
    data = Aspirant.objects.all()
    return render(request,'app1/List.html',{'data1':data,})

def Communication(request):
    message = ''
    if request.method == 'POST':
        data = request.POST
        message = 'The upload is sucessfull'
        form = RoundComForm(request.POST)
        if form.is_valid():
            form.save()
            form = RoundComForm()
        else:
            message ='The upload is not sucessfull'
    else:
        form = RoundComForm()
        message = 'The upload is not sucessfull'
    return render(request,'app1/Communication.html',{'message':message,'form':form})

def Technical(request):
    message = ''
    if request.method == 'POST':
        data = request.POST
        message = 'The upload is sucessfull'
        form = RoundTechForm(request.POST)
        if form.is_valid():
            form.save()
            form = RoundTechForm()
        else:
            message ='The upload is not sucessfull'
    else:
        form = RoundTechForm()
        message = 'The upload is not sucessfull'
    return render(request,'app1/Technical.html',{'message':message,'form':form})

def CEO(request):
    message = ''
    if request.method == 'POST':
        data = request.POST
        message = 'The upload is sucessfull'
        form = RoundCEOForm(request.POST)
        if form.is_valid():
            form.save()
            form = RoundCEOForm()
        else:
            message ='The upload is not sucessfull'
    else:
        form = RoundCEOForm()
        message = 'The upload is not sucessfull'
    return render(request,'app1/CEO.html',{'message':message,'form':form})




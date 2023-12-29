from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Aspirant,Rounds,Onboared
from .forms import AspirantForm
# Create your views here.


def add_aspirant_view(request):
    message=''
    
    if request.method=='POST':
        form=AspirantForm(request.POST)
        if form.is_valid():
            form.save()
            message='Application created successful.'
    else:
        message=''
        form=AspirantForm()
    fm = Aspirant.objects.all() 
    return render(request,'addaspirant.html',{'message':message,'form':form,'fm':fm})

def aspirant_view(request):
    data=Aspirant.objects.all()
    return render(request,'aspirant.html',{'data':data})

def update_aspirant_view(request,id):
    if request.method=='POST':
        data=Aspirant.objects.get(pk=id)
        form1=AspirantForm(request.POST,instance=data)
        if form1.is_valid():
            form1.save()
    else:
        data=Aspirant.objects.get(pk=id)
        form1=AspirantForm(instance=data)
    return render(request,'update.html',{'form':form1})

def delete_aspirant_view(request,id):
    if request.method=='POST':
        data=Aspirant.objects.get(pk=id)
        data.delete()
    return HttpResponseRedirect('/aspirant/')


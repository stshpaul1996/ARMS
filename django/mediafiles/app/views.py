from django.shortcuts import render,redirect
from .forms import CricketerForm
from .models import Cricketer
# Create your views here.


def add_cricketer(request):
    errors=''
    if request.method=='POST':
        data=request.POST
        form = CricketerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            errors=form.errors
            return redirect('/')
            #return render(request,'addcricketer.html',{'form':form,'errors':errors})
    else:
        form=CricketerForm()
    return render(request,'addcricketer.html',{'form':form})

def cricketer(request):
    data=Cricketer.objects.all()
    return render(request,'cricketer.html',{'data':data,'hedders':'List of Crickters'})
        
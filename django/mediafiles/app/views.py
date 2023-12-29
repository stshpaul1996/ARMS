from django.shortcuts import render,redirect,HttpResponseRedirect
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
            return render(request,'addcricketer.html',{'form':form,'errors':errors})
    else:
        form=CricketerForm()
    return render(request,'addcricketer.html',{'form':form})

def cricketer(request):
    data=Cricketer.objects.all()
    return render(request,'cricketer.html',{'data':data,'hedders':'List of Crickters'})
        
def delete(request,id):
    if request.method == 'POST':
        pi = Cricketer.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/cricketer/')

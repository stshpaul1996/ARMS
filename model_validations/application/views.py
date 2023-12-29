from django.shortcuts import render,redirect
from . forms import AspirantForm
from . models import Aspirant
# Create your views here.
def adding(request):
    form=AspirantForm()
    if request.method == 'POST':
        form=AspirantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/dis/")
    return render(request,"application/register.html",{"form":form})

def display(request):
    d=Aspirant.objects.all()
    return render(request,"application/display.html",{"d":d})
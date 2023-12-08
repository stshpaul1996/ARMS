from django.shortcuts import render, redirect

from .forms import FormResources
from .models import Resources
from django.http import HttpResponse

# Create your views here.
def form_view(request):
   
    form = FormResources()
    if request.method == "POST":
        form = FormResources(request.POST)
        if form.is_valid():
            form.save()
            return redirect("data/")
              
    return render(request, "form.html", {"form":form})


def register_view(request):
    msg = "You have successfully registered"
    data = Resources.objects.all()
    return render(request, "header.html", {"data": data, "msg":msg})

    
    
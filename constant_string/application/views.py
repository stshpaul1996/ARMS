from django.shortcuts import render
from django.http import HttpResponse
from . constants import data
from .models import display
# Create your views here.

def displays(request,name):
    for i,j in data.items():
        if i==name:
            var=j
            return render(request,"application/index.html",{"var":var})
    return HttpResponse(name)

def movie(request):
    m=display.objects.all()
    return render(request,"application/movie.html",{"m":m})
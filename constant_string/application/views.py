from django.shortcuts import render
from django.http import HttpResponse
from . constants import data
# Create your views here.

def display(request,name):
    for i,j in data.items():
        if i==name:
            var=j
            return render(request,"application/index.html",{"var":var})
    return HttpResponse(name)

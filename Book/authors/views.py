from django.shortcuts import render
from .constants import details
from django.http import HttpResponse

def Details(request,name):
    auth_detail=details.get(name)
    if auth_detail:
        return render(request,'app1/index.html',{'auth_details':auth_detail})
    else:
        return HttpResponse(name)

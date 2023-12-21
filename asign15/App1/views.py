from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Entrepreneur

def entrepreneur_details_view(request):
    details = Entrepreneur.objects.all()
    if details:
        return render(request,"app1/index.html",{"details":details})
    else:
        return HttpResponse()
    

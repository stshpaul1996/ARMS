from django.shortcuts import render
from App1.constants import person_details
from django.http import HttpResponse

def Person_detail(request, name):
    details = person_details.get(name)
    
    if details:
        return render(request, 'app1/index.html', {'details': details,'name':name})
    else:
        return render(request, 'app1/index.html', {'name': name})
    
# Create your views here.

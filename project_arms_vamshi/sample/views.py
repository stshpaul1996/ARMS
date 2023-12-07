from django.shortcuts import render
from django.http import HttpResponse
import os

def hello(request):
    value = os.environ.get('crazy')
    print(dir(os))
    return HttpResponse(value)
def login(request):
    os.environ['tejus'] = 'fighter Jet'
    value = os.environ.get('tejus')
    return HttpResponse(value)



    





















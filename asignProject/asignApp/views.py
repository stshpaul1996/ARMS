from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import os
import platform

def get_os(request):
    name = platform.system()
    return HttpResponse(name)

def s_var(request):
    os.environ['var']='nithisha'
    value=os.environ.get('var')
    return HttpResponse(value)
 
def p_var(request):
    
    value=os.environ.get('my_var')
    return HttpResponse(value)

def set_env(request):
    os.environ["ses_var"] = "Hello Session Variable"
    return HttpResponse(os.environ.get("ses_var"))

def get_env(request):
   
    return HttpResponse(os.environ.get("ses_var"))
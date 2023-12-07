from django.shortcuts import render
import os
from django.http import HttpResponse
# Create your views here.

def my_view(request):
    
    env_var = os.environ.get('my_variable')
    # print(os.environ)
    # print("my_view : {}".format(env_var))
    
    return HttpResponse(env_var)  
  


def temp_var(request):
    os.environ['temp_variable'] = "This is Temp variable"
    var = os.environ.get('temp_variable')
    return HttpResponse(var)
from django.shortcuts import render
import os
from django.http import HttpResponse
# Create your views here.

def my_view(request):
    
    env_var = os.environ.get('var')
    # print(os.environ)
    # print("my_view : {}".format(env_var))
    
    return HttpResponse(env_var)  
  


def temp_var(request):
    os.environ['temp_variable'] = "This is session  variable"
    var = os.environ.get('temp_variable')
    return HttpResponse(var)
from django.shortcuts import render
from django.http import HttpResponse
import os, sys

def func(request):
    arguments = os.environ.get('var')
    print(arguments)
    return HttpResponse(arguments)

def set_var(request):
    os.environ['var1'] = 's'
    # print(var)
    return HttpResponse('<h1>session variable created</h1>')

def get_var(reques):
    return HttpResponse(os.environ.get('var1'))

def os_name(reques):
    name = os.name
    return HttpResponse(name)
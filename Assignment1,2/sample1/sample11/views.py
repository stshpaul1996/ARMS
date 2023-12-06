from django.shortcuts import render
import os
from django.http import HttpResponse
def get_harini(request):
    value=os.environ.get('result')
    return HttpResponse(value)
def get_hello(request):
    os.environ['a'] = 'haritha'
    value = os.environ.get('a')
    return HttpResponse(value)
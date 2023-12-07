from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import os

def task1(request):
    result1=os.environ.get('my_variable','defualt')
    result2=os.environ.get('my_variable1','defualt')
    return HttpResponse(f'result1:{result1},result2:{result2}')

  

def set_session(request):
    os.environ['variable']='hello world'
    return HttpResponse(os.environ.get('variable'))

def get_session(request):
    session_user = os.environ.get('variable')
    return HttpResponse(session_user)


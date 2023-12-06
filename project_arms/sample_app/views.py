from django.shortcuts import render

from django.http import HttpResponse
# def homePage(request):
#     x="welcome to Django session"
#     return HttpResponse(x)

def greet(request):
    os.environ['r']='rami'
    value=os.environ.get('r')
    return HttpResponse(value)
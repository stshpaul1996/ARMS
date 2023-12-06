from django.shortcuts import render
# create sample project, one application. write below urls 
#     /ram.  add this url in project.urls. write the definition of function in project.urls. return size of the ram of your machine as response
#     /os. add this url in project.urls. write the definition of function in application.views. return os name of your machine as response
#     /ncores. add this url in project.urls. write the definition of function in application.own_views. return number of cores of your machine as response
#     /users. add this url in project.urls. write the definition of function in project.own_views. return some html code as response
import os
import psutil
import platform
from django.http import HttpResponse
def ram(request):
    value=psutil.virtual_memory().total
    return HttpResponse(value)
def os_information(request):
    value=platform.system()
    return HttpResponse(value)
def ncores(request):
    value=psutil.cpu_count(logical=False)
    return HttpResponse(value)
def users_information(request):
    html_response="<html><body><h1>Hi Users</h1></body></html>" 
    return HttpResponse(html_response)   
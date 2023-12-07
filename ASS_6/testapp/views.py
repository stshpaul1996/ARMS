from django.shortcuts import render

from django.http import HttpResponse


import socket


"""  

5) create sample project, one application. write below urls 
    /ram.  add this url in project.urls. write the definition of function in project.urls. return size of the ram of your machine as response
    /os. add this url in project.urls. write the definition of function in application.views. return os name of your machine as response
    /ncores. add this url in project.urls. write the definition of function in application.own_views. return number of cores of your machine as response
    /users. add this url in project.urls. write the definition of function in project.own_views. return some html code as response


"""

host_name = socket.gethostname()

def machine_name(request):
    return HttpResponse("this is machine name : {}".format(host_name))


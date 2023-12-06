from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.
def os_name(request):
    return HttpResponse("os name is={}".format(os.name))
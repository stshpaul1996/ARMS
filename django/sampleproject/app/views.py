from django.shortcuts import render
from django.http import HttpResponse
import os
import platform

# Create your views here.
def get_os_name(request):
    os_name = platform.system()
    print(dir(platform))
    return HttpResponse(f"Operating System: {os_name}")
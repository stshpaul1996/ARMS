from django.shortcuts import render
from django.http import HttpResponse
import platform
import os
import multiprocessing

def get_os_name(request):
    os_name=platform.system()
    return HttpResponse(f'your os name:{os_name} ')


def get_cores(request):
    num_cores=multiprocessing.cpu_count()
    return HttpResponse(f'your number of cores: {num_cores}')

def code(request):
    return HttpResponse('<h1>this html</h1>')
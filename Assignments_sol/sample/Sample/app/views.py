from django.shortcuts import render
import psutil
from django.http import JsonResponse,HttpResponse
import os
import multiprocessing


def get_ram_size(request):
    r_size = psutil.virtual_memory().total
    ram_size_gb = r_size / (1024 ** 3)
    print(ram_size_gb)
    return JsonResponse({'ram_size_gb': ram_size_gb})


def num_cores(request):
    num_cores = multiprocessing.cpu_count()
    return JsonResponse({'num_cores': num_cores})
def html_res(request):
    return HttpResponse('<h1>hello world</h1>')

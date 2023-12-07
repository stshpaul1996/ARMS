from django.shortcuts import render
from django.http import HttpResponse
import multiprocessing

def get_number_of_cores(request):
    num_cores = multiprocessing.cpu_count()
    return HttpResponse(f"Number of Cores: {num_cores}")

def custom_users_view(request):
    html_response = "<h1>Custom Users View</h1><p>Hii... This is a html page.</p>"
    return HttpResponse(html_response)

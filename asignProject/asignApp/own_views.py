import os
from django.http import HttpResponse

def get_ncores(request):
    Number_of_cores = os.cpu_count()
    return HttpResponse(Number_of_cores)
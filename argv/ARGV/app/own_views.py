from django.http import HttpResponse
import os

def cores(request):
    no_cor = os.cpu_count()
    return HttpResponse(no_cor)
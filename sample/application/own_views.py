from django.http import HttpResponse
import psutil
def no_of_curs(request):
    return HttpResponse("no of cores of my machine is={}".format(psutil.cpu_count()))
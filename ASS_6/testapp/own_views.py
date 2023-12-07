import multiprocessing

from django.http import HttpResponse

num_cores = multiprocessing.cpu_count()

def no_of_cores(request):
    return HttpResponse('No_of_cores_of_machine :{}'.format(num_cores))
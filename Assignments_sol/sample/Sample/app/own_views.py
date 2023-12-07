import multiprocessing
from django.http import JsonResponse
def num_cores(request):
    num_cores = multiprocessing.cpu_count()
    return JsonResponse({'num_cores': num_cores})
import os
from django.http import JsonResponse
def os_name(request):
    os_name = os.name
    return JsonResponse({'os_name': os_name})


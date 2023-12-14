from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Cricketers
#from .constants import data

# Create your views here.
def cricketers_view(request):
    data = Cricketers.objects.all()
    return render(request, "app1/cricketers.html", 
                  {"cricketers_data": data, "header": "LIST OF CRICKETERS"})

def cricketer_view_id(request, cricketer_id):
    import pdb;pdb.set_trace()
    type_data = str(type(cricketer_id))
    return HttpResponse("id"+str(cricketer_id))

def cricketer_view(request, cricketer):
    type_data = str(type(cricketer))
    return HttpResponse("name"+cricketer)


def home_view(request):
    return render(request, "app1/home.html")

def kohli_view(request):
    return render(request, "app1/kohli.html")

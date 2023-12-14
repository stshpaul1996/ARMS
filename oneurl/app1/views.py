from django.shortcuts import render
from .constants import data
from django.http import HttpResponse

# Create your views here.
def oneurl(request,name1):
    for key, value in data.items():
        if name1 == key:
            var = value
    # for i in context(data.keys()):
    #     var = i
    #     if name1 == i:
            return render(request,'app1/index.html',{'var':var,'name1':key})
    else:
        return HttpResponse(name1)

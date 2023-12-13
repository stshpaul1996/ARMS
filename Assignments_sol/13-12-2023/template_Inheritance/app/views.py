from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .contraints import cricketers_data
# Create your views here.

def personalities(request,name):
    if name in cricketers_data.keys():
        image=cricketers_data[name]['image']
        content=cricketers_data[name]['content']
        return render(request,'cricketers.html',{'image':image,'content':content,'name':name})
    else :
        return HttpResponse('<h1>no persons here</h1>')
from django.shortcuts import render
from .models import Gun
from django.http import HttpResponse

# Create your views here.
def wep(request,name1):
    data = Gun.objects.all()
    for i in data:
        if i.name == name1:
            return render(request,'app1/index.html',{'data1':data})
    else:
        return HttpResponse(name1)
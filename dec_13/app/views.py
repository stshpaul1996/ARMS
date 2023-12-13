from django.shortcuts import render
from django.http import HttpResponse
from app.constants import travel_details

# Create your views here.
def Travel(request,name):
    result = travel_details.get(name)

    if result:
        return render(request,"app/home.html",{"result":result,"name":name})
    else:
        return HttpResponse(name)

    
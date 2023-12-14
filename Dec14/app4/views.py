from django.shortcuts import render
from django.http import HttpResponse
from app4.models import Tourist_places

# Create your views here.
def Tourist_view(request):
    data=Tourist_places.objects.all()
    return render(request,"tourist.html" ,{"result":data})
from django.shortcuts import render
from .models import employee
# Create your views here.
def show_data(request):
    q=employee.objects.all()
    return render(request,'app1/home.html',{'data':q})

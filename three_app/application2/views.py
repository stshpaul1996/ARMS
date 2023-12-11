from django.shortcuts import render

# Create your views here.
def display2(request):
    return render(request,'app2/temp1.html')
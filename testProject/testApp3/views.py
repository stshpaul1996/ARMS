from django.shortcuts import render

# Create your views here.
def app3(request):
    return render(request,"App3/index.html")
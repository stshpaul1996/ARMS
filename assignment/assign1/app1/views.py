from django.shortcuts import render

# Create your views here.
def application1(request):
    return render(request,"app1/index.html")

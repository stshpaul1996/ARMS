from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,"app1/comhome.html")

def veg_view(request):
    return render(request,"app1/veg.html")
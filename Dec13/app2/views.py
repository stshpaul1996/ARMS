from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"app2/home.html")
def taj(request):
    return render(request,"app2/1taj.html")
def sob(request):
    return render(request,"app2/2sob.html")
def eiffeltower(request):
    return render(request,"app2/3eiffeltower.html")
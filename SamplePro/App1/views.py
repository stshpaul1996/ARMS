from django.shortcuts import render


# Create your views here.
def app_one(request):
     return render(request, "App1/index.html")
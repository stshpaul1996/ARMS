from django.shortcuts import render

# Create your views here
def app_one(request):
     return render(request, "App3\index.html")
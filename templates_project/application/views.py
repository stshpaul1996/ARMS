from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'application/home.html')

def animal_view(request):
    return render(request, 'application/animal.html')

def hi_nanna_view(request):
    return render(request, 'application/hi_nanna.html')

def kotabomalli_view(request):
    return render(request, 'application/kotabomalli.html')

def extra_view(request):
    return render(request, 'application/extra.html')
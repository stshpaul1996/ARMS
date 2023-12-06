from django.http import HttpResponse
def display(request):
    return HttpResponse("<h1>Hello everyone welcome to django</h1>")
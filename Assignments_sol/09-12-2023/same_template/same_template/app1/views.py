from django.shortcuts import render

def app1_show(request):
    return render(request, 'app1/test.html')
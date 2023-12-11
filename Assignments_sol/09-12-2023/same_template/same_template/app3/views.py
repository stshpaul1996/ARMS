from django.shortcuts import render

def app3_show(request):
    return render(request, 'app3/test.html')
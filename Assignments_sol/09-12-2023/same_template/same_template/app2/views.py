from django.shortcuts import render

def app2_show(request):
    return render(request, 'app2/test.html')
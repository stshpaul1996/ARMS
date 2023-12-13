from django.shortcuts import render

def display(request):
    return render(request,'app1/base_home.html')
def show_cric(request):
    return render(request,'app1/cric.html')
from django.shortcuts import  render

def temp_fun(request):
    return render(request,'testapp/app.html')
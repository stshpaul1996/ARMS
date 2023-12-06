from django.http import HttpResponse

def html_fun(request):
    return HttpResponse('<h1> this is html code function execution </h1>' )
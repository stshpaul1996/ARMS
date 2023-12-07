from django.http import HttpResponse 

def get_html(request):
    code = "<h1>Welcome to Django Framework</h1>"
    return HttpResponse(code)
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def base_customer_create_view(request):
    return render(request, "customer_create.html")
     # it will read the code from customer_create.html
     # this forms a http response 
    


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def base_customer_create_view(request):
 #   return HttpResponse("customer created")
def base_customer_create_view(request):
    return render(request,"basetemplate/customer_create.html")   
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#def person1_create_view(request):
 #   return HttpResponse("person created")
def person1_create_view(request):
    return render(request,"sampletemplate/customer_create.html")      
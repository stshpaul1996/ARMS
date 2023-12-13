from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .constants import data


def home_view(request):
    data = "<h1>Welcome to page of Great Leaders</h1>"
    return HttpResponse(data)

def details_view(request, name):
    
    for i,j in data.items():
        persons = ['patal', 'ambedkar', 'apj', 'atal', 'baba', 'teresa', 'nehru', 'chari', 'gandhi']
        
        if i == name:
            var = j
            persons.remove(i)
        
            #persons_str = ','.join(persons)
            
            return render(request, "app2/index.html",{'var':var, 'name':name, 'persons':persons})
        
       

    
    return HttpResponse(name)
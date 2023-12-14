from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Person


def home_view(request):
    data = "<h1>Welcome to page of Great Leaders</h1>"
    return HttpResponse(data)

def details_view(request, name):

    get_persons = Person.objects.all()

    # for i,j in enumerate(get_persons):
    #     persons = [ 'ambedkar', 'apj', 'gandhi', 'chari', 'patal', 'nehru', 'teresa','atal', 'baba']
        
    #     if name == persons[i]:

    #         persons.remove(name)
            
    return render(request, "app2/index.html", {'content': get_persons})
        
    